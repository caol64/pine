import ctypes
import os
import platform
from ctypes import c_void_p, c_uint, c_ulong, c_char, c_bool


# we get the correct library extension per os
lib="libpine_c"
cur_os = platform.system()
if(cur_os == "Linux"):
    lib="libpine_c.so"
elif(cur_os == "Windows"):
    lib="libpine_c.dll"
elif(cur_os == "Darwin"):
    lib="libpine_c.dylib"


# we load the library, this will require it to be in the same folder
# refer to bindings/c to build the library.
libipc = ctypes.CDLL(os.path.join(os.path.dirname(os.path.abspath(__file__)),lib))

libipc.pine_pcsx2_new.restype = c_void_p

libipc.pine_read.argtypes = [c_void_p, c_uint, c_char, c_bool]
libipc.pine_read.restype = c_ulong

libipc.pine_get_error.argtypes = [c_void_p]
libipc.pine_get_error.restype = c_uint

libipc.pine_pcsx2_delete.argtypes = [c_void_p]
libipc.pine_pcsx2_delete.restype = None

ipc = libipc.pine_pcsx2_new()
value = libipc.pine_read(ipc, 0x00347D34, c_char(0), False)
print("Read:", value)
print("Error:", libipc.pine_get_error(ipc))
libipc.pine_pcsx2_delete(ipc)
