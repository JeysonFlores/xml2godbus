template = """// this file was generated by xml2godbus. You probably have to edit this file
package {package_name}

import (
	"github.com/godbus/dbus/v5"
	"github.com/godbus/dbus/v5/introspect"
)

type {iface_name} struct {{
    bus *dbus.Conn
}}

{methods}

{signals}

{util_functions}

"""


def create_template():
    return template


# TODO: Custom structure type
def get_type(type):
    if len(type) == 1:
        if type == "y":
            return "byte"
        elif type == "b":
            return "bool"
        elif type == "n":
            return "int16"
        elif type == "q":
            return "uint16"
        elif type == "i":
            return "int"
        elif type == "u":
            return "uint"
        elif type == "x":
            return "int64"
        elif type == "t":
            return "uint64"
        elif type == "d":
            return "float64"
        elif type == "s":
            return "string"
    elif len(type) == 2 and type[0] == "a":
        return "[]" + get_type(type[1])
    elif (
        type[0] == "a"
        and type.find("{") != -1
        and type.find("}") != -1
        and (type.find("}") - type.find("{")) == 3
    ):
        return "map[" + get_type(type[2]) + "]" + get_type(type[3])


def parse_arg(arg, signal):
    if signal:
        return arg["@name"], get_type(arg["@type"])
    else:
        if not "@direction" in arg:
            return get_type(arg["@type"])
        else:
            if arg["@direction"] == "in":
                return arg["@name"] + " " + get_type(arg["@type"])
            if arg["@direction"] == "out":
                return get_type(arg["@type"])


def mix_args(names, datatypes):
    for i in range(0, names):
        pass


def create_method(iface_name, method):
    in_args = ""
    out_args = ""
    for arguments in method["arg"]:
        if len(arguments) > 0:
            if arguments["@direction"] == "in":
                in_args += parse_arg(arguments, False) + ","
            elif arguments["@direction"] == "out":
                out_args += parse_arg(arguments, False) + ","
    abr = iface_name[0].lower()
    method_name = method["@name"]
    base = (
        "func ("
        + abr
        + " *"
        + iface_name
        + ") "
        + method_name
        + "("
        + in_args[:-1]
        + ") ("
        + out_args
        + "*dbus.Error) { \n}\n\n"
    )
    return base


def create_signal(iface_name, signal):
    out_args = ""
    out_args_names = ""
    for arguments in signal["arg"]:
        if len(arguments) > 0:
            if "@direction" in arguments:
                if arguments["@direction"] == "in":
                    continue
            arg_name, arg_datatype = parse_arg(arguments, True)
            out_args_names += arg_name + ","
            out_args += arg_name + " " + arg_datatype + ","
    abr = iface_name[0].lower()
    signal_name = signal["@name"]
    base = """func ({abr} *{iface_name}) Emit{signal_name}Signal({out_args}) {{
    {abr}.bus.Emit({abr}.GetObjectPath(), {abr}.GetInterfacePath()+".{signal_name}", {out_args_names})
}}\n\n""".format(
        abr=abr,
        iface_name=iface_name,
        signal_name=signal_name,
        out_args=out_args[:-1],
        out_args_names=out_args_names[:-1],
    )
    return base


def create_utils(iface, intro):
    iface_name = iface[::-1].split(".", 1)[0][::-1]
    abr = iface_name[0].lower()
    obj_path = iface.replace(".", "/")
    get_obj_func = """func ({abr} *{iface_name}) GetObjectPath() dbus.ObjectPath {{
	return dbus.ObjectPath("{obj_path}")
}}""".format(
        abr=abr, iface_name=iface_name, obj_path=obj_path
    )

    get_iface_func = """func ({abr} *{iface_name}) GetInterfacePath() string {{
	return "{iface}"
}}""".format(
        abr=abr, iface_name=iface_name, iface=iface
    )

    get_intro_func = """func ({abr} *{iface_name}) GetIntroData() string {{
        return `{intro}`
}}""".format(
        abr=abr, iface_name=iface_name, intro=intro
    )

    return get_obj_func, get_iface_func, get_intro_func
