# xml2godbus
Parse your XML introspection file for DBus to the godbus library.
> Note: This is work in progress, it may not work properly for some specific use cases

### Supported features:
- [x] Methods
- [x] Signals
- [ ] Properties

### Supported datatypes:
- [x] byte | BYTE
- [x] bool | BOOLEAN
- [x] int16 | INT16
- [x] uint16 | UINT16
- [x] int | INT32
- [x] uint | UINT32
- [x] int32 | INT32
- [x] uint32 | UINT32
- [x] int64 | INT64
- [x] uint64 | UINT64
- [x] float64 | DOUBLE
- [x] string | STRING
- [ ] ObjectPath | OBJECT_PATH
- [ ] Signature | SIGNATURE
- [ ] Variant | VARIANT
- [ ] interface{} | VARIANT
- [ ] UnixFDIndex | UNIX_FD
- [x] array | ARRAY
- [x] map | DICT
- [ ] struct | STRUCT

## Build & Installation
### Dependencies
```
- click (8.0.3)
- xmltodict (0.12.0)
```
To install them just run:
```
pip3 install click xmltodict
```
### Build
  ```
git clone https://github.com/JeysonFlores/xml2godbus
cd xml2godbus
sudo python3 setup.py install
```
### Run
```
xml2-godbus --xml MyFile.xml
```