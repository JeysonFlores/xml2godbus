import xmltodict, json
from template import *


class Interface(object):
    def __init__(self, file):
        f = open(file, "r")
        self.file = f.read()
        self.data = json.loads(json.dumps(xmltodict.parse(self.file)))
        self.data["node"]["interface"] = self.dict_to_list(
            self.data["node"]["interface"]
        )
        self.iface = self.data["node"]["interface"][0]

    def dict_to_list(self, some_dic):
        if type(some_dic) == list:
            return some_dic
        return [some_dic]

    def generate_methods(self):
        self.methods = "//Methods\n"
        for method in self.dict_to_list(self.iface["method"]):
            if type(method["arg"]) == dict:
                method["arg"] = self.dict_to_list(method["arg"])

            self.methods += create_method(
                self.iface["@name"][::-1].split(".", 1)[0][::-1], method
            )
        pass

    def generate_signals(self):
        self.signals = "//Signals\n"
        for signal in self.dict_to_list(self.iface["signal"]):
            if type(signal["arg"]) == dict:
                signal["arg"] = self.dict_to_list(signal["arg"])
            self.signals += create_signal(
                self.iface["@name"][::-1].split(".", 1)[0][::-1], signal
            )

    def generate_utils(self):
        self.utils = "//Utils\n"
        obj_func, iface_path_func, intro_func = create_utils(
            self.iface["@name"], self.file
        )
        self.utils += obj_func + "\n\n" + iface_path_func + "\n\n" + intro_func

    def generate_file(self):
        self.generate_methods()
        self.generate_signals()
        self.generate_utils()

        interface_name = self.iface["@name"][::-1].split(".", 1)[0][::-1]
        final_file = template.format(
            package_name=interface_name.lower(),
            iface_name=interface_name,
            signals=self.signals,
            util_functions=self.utils,
            methods=self.methods,
        )
        new_file = open(interface_name.lower() + ".go", "a")
        new_file.write(final_file)
        new_file.close()
