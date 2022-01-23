// this file was generated by xml2godbus. You probably have to edit this file
package regex

import (
	"github.com/godbus/dbus/v5"
	"github.com/godbus/dbus/v5/introspect"
)

type Regex struct {
    bus *dbus.Conn
}

//Methods
func (r *Regex) GetRegexes() (map[int]string,*dbus.Error) { 
}

func (r *Regex) GetRegexById(id int) (map[int]string,*dbus.Error) { 
}

func (r *Regex) SetRegex(name string,regex string,example string) (bool,*dbus.Error) { 
}

func (r *Regex) UpdateRegex(id int,name string,regex string,example string) (bool,*dbus.Error) { 
}

func (r *Regex) DeleteRegex(id int) (bool,*dbus.Error) { 
}



//Signals
func (r *Regex) EmitRegexAddedSignal(id int,name string,regex string,example string) {
    r.bus.Emit(r.GetObjectPath(), r.GetInterfacePath()+".RegexAdded", id,name,regex,example)
}

func (r *Regex) EmitRegexUpdatedSignal(id int,name string,regex string,example string) {
    r.bus.Emit(r.GetObjectPath(), r.GetInterfacePath()+".RegexUpdated", id,name,regex,example)
}

func (r *Regex) EmitRegexDeletedSignal(id int) {
    r.bus.Emit(r.GetObjectPath(), r.GetInterfacePath()+".RegexDeleted", id)
}



//Utils
func (r *Regex) GetObjectPath() dbus.ObjectPath {
	return dbus.ObjectPath("com/github/jeysonflores/Regex")
}

func (r *Regex) GetInterfacePath() string {
	return "com.github.jeysonflores.Regex"
}

func (r *Regex) GetIntroData() string {
        return `<?xml version="1.0" encoding="UTF-8"?>

<node>
    <interface name="com.github.jeysonflores.Regex">

        <method name="GetRegexes">
            <arg type="a{is}" name="regexes" direction="out" />
        </method> 

        <method name="GetRegexById">
            <arg type="i" name="id" direction="in" />
            <arg type="a{is}" name="regex" direction="out" />
        </method>

        <method name="SetRegex">
            <arg type="s" name="name" direction="in" />
            <arg type="s" name="regex" direction="in" />
            <arg type="s" name="example" direction="in" />
            <arg type="b" name="was_completed" direction="out" />
        </method>

        <method name="UpdateRegex">
            <arg type="i" name="id" direction="in" />
            <arg type="s" name="name" direction="in" />
            <arg type="s" name="regex" direction="in" />
            <arg type="s" name="example" direction="in" />
            <arg type="b" name="was_completed" direction="out" />
        </method>

        <method name="DeleteRegex">
            <arg type="i" name="id" direction="in" />
            <arg type="b" name="was_completed" direction="out" />
        </method>

        <signal name="RegexAdded">
            <arg type="i" name="id" />
            <arg type="s" name="name" />
            <arg type="s" name="regex" />
            <arg type="s" name="example" />
        </signal>

        <signal name="RegexUpdated">
            <arg type="i" name="id" />
            <arg type="s" name="name" />
            <arg type="s" name="regex" />
            <arg type="s" name="example" />
        </signal>

        <signal name="RegexDeleted">
            <arg type="i" name="id" />
        </signal>

    </interface>
</node>`
}

