# Python stubs generated by omniidl from ..\..\..\..\..\idl\compression.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


# #include "corbaidl.idl"
import corbaidl_idl
_0_CORBA = omniORB.openModule("omniORB.CORBA")
_0_CORBA__POA = omniORB.openModule("omniORB.CORBA__POA")

#
# Start of module "Compression"
#
__name__ = "omniORB.Compression"
_0_Compression = omniORB.openModule("omniORB.Compression", r"..\..\..\..\..\idl\compression.idl")
_0_Compression__POA = omniORB.openModule("omniORB.Compression__POA", r"..\..\..\..\..\idl\compression.idl")


# exception CompressionException
_0_Compression.CompressionException = omniORB.newEmptyClass()
class CompressionException (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/Compression/CompressionException:1.0"

    def __init__(self, reason, description):
        CORBA.UserException.__init__(self, reason, description)
        self.reason = reason
        self.description = description

_0_Compression.CompressionException = CompressionException
_0_Compression._d_CompressionException  = (omniORB.tcInternal.tv_except, CompressionException, CompressionException._NP_RepositoryId, "CompressionException", "reason", omniORB.tcInternal.tv_long, "description", (omniORB.tcInternal.tv_string,0))
_0_Compression._tc_CompressionException = omniORB.tcInternal.createTypeCode(_0_Compression._d_CompressionException)
omniORB.registerType(CompressionException._NP_RepositoryId, _0_Compression._d_CompressionException, _0_Compression._tc_CompressionException)
del CompressionException

# exception FactoryAlreadyRegistered
_0_Compression.FactoryAlreadyRegistered = omniORB.newEmptyClass()
class FactoryAlreadyRegistered (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/Compression/FactoryAlreadyRegistered:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_Compression.FactoryAlreadyRegistered = FactoryAlreadyRegistered
_0_Compression._d_FactoryAlreadyRegistered  = (omniORB.tcInternal.tv_except, FactoryAlreadyRegistered, FactoryAlreadyRegistered._NP_RepositoryId, "FactoryAlreadyRegistered")
_0_Compression._tc_FactoryAlreadyRegistered = omniORB.tcInternal.createTypeCode(_0_Compression._d_FactoryAlreadyRegistered)
omniORB.registerType(FactoryAlreadyRegistered._NP_RepositoryId, _0_Compression._d_FactoryAlreadyRegistered, _0_Compression._tc_FactoryAlreadyRegistered)
del FactoryAlreadyRegistered

# exception UnknownCompressorId
_0_Compression.UnknownCompressorId = omniORB.newEmptyClass()
class UnknownCompressorId (CORBA.UserException):
    _NP_RepositoryId = "IDL:omg.org/Compression/UnknownCompressorId:1.0"

    def __init__(self):
        CORBA.UserException.__init__(self)

_0_Compression.UnknownCompressorId = UnknownCompressorId
_0_Compression._d_UnknownCompressorId  = (omniORB.tcInternal.tv_except, UnknownCompressorId, UnknownCompressorId._NP_RepositoryId, "UnknownCompressorId")
_0_Compression._tc_UnknownCompressorId = omniORB.tcInternal.createTypeCode(_0_Compression._d_UnknownCompressorId)
omniORB.registerType(UnknownCompressorId._NP_RepositoryId, _0_Compression._d_UnknownCompressorId, _0_Compression._tc_UnknownCompressorId)
del UnknownCompressorId

# typedef ... CompressorId
class CompressorId:
    _NP_RepositoryId = "IDL:omg.org/Compression/CompressorId:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Compression.CompressorId = CompressorId
_0_Compression._d_CompressorId  = omniORB.tcInternal.tv_ushort
_0_Compression._ad_CompressorId = (omniORB.tcInternal.tv_alias, CompressorId._NP_RepositoryId, "CompressorId", omniORB.tcInternal.tv_ushort)
_0_Compression._tc_CompressorId = omniORB.tcInternal.createTypeCode(_0_Compression._ad_CompressorId)
omniORB.registerType(CompressorId._NP_RepositoryId, _0_Compression._ad_CompressorId, _0_Compression._tc_CompressorId)
del CompressorId
_0_Compression.COMPRESSORID_NONE = 0
_0_Compression.COMPRESSORID_GZIP = 1
_0_Compression.COMPRESSORID_PKZIP = 2
_0_Compression.COMPRESSORID_BZIP2 = 3
_0_Compression.COMPRESSORID_ZLIB = 4
_0_Compression.COMPRESSORID_LZMA = 5
_0_Compression.COMPRESSORID_LZO = 6
_0_Compression.COMPRESSORID_RZIP = 7
_0_Compression.COMPRESSORID_7X = 8
_0_Compression.COMPRESSORID_XAR = 9

# typedef ... CompressionLevel
class CompressionLevel:
    _NP_RepositoryId = "IDL:omg.org/Compression/CompressionLevel:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Compression.CompressionLevel = CompressionLevel
_0_Compression._d_CompressionLevel  = omniORB.tcInternal.tv_ushort
_0_Compression._ad_CompressionLevel = (omniORB.tcInternal.tv_alias, CompressionLevel._NP_RepositoryId, "CompressionLevel", omniORB.tcInternal.tv_ushort)
_0_Compression._tc_CompressionLevel = omniORB.tcInternal.createTypeCode(_0_Compression._ad_CompressionLevel)
omniORB.registerType(CompressionLevel._NP_RepositoryId, _0_Compression._ad_CompressionLevel, _0_Compression._tc_CompressionLevel)
del CompressionLevel

# typedef ... CompressionRatio
class CompressionRatio:
    _NP_RepositoryId = "IDL:omg.org/Compression/CompressionRatio:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Compression.CompressionRatio = CompressionRatio
_0_Compression._d_CompressionRatio  = omniORB.tcInternal.tv_float
_0_Compression._ad_CompressionRatio = (omniORB.tcInternal.tv_alias, CompressionRatio._NP_RepositoryId, "CompressionRatio", omniORB.tcInternal.tv_float)
_0_Compression._tc_CompressionRatio = omniORB.tcInternal.createTypeCode(_0_Compression._ad_CompressionRatio)
omniORB.registerType(CompressionRatio._NP_RepositoryId, _0_Compression._ad_CompressionRatio, _0_Compression._tc_CompressionRatio)
del CompressionRatio

# struct CompressorIdLevel
_0_Compression.CompressorIdLevel = omniORB.newEmptyClass()
class CompressorIdLevel (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/Compression/CompressorIdLevel:1.0"

    def __init__(self, compressor_id, compression_level):
        self.compressor_id = compressor_id
        self.compression_level = compression_level

_0_Compression.CompressorIdLevel = CompressorIdLevel
_0_Compression._d_CompressorIdLevel  = (omniORB.tcInternal.tv_struct, CompressorIdLevel, CompressorIdLevel._NP_RepositoryId, "CompressorIdLevel", "compressor_id", omniORB.typeMapping["IDL:omg.org/Compression/CompressorId:1.0"], "compression_level", omniORB.typeMapping["IDL:omg.org/Compression/CompressionLevel:1.0"])
_0_Compression._tc_CompressorIdLevel = omniORB.tcInternal.createTypeCode(_0_Compression._d_CompressorIdLevel)
omniORB.registerType(CompressorIdLevel._NP_RepositoryId, _0_Compression._d_CompressorIdLevel, _0_Compression._tc_CompressorIdLevel)
del CompressorIdLevel

# typedef ... CompressorIdLevelList
class CompressorIdLevelList:
    _NP_RepositoryId = "IDL:omg.org/Compression/CompressorIdLevelList:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Compression.CompressorIdLevelList = CompressorIdLevelList
_0_Compression._d_CompressorIdLevelList  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/Compression/CompressorIdLevel:1.0"], 0)
_0_Compression._ad_CompressorIdLevelList = (omniORB.tcInternal.tv_alias, CompressorIdLevelList._NP_RepositoryId, "CompressorIdLevelList", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/Compression/CompressorIdLevel:1.0"], 0))
_0_Compression._tc_CompressorIdLevelList = omniORB.tcInternal.createTypeCode(_0_Compression._ad_CompressorIdLevelList)
omniORB.registerType(CompressorIdLevelList._NP_RepositoryId, _0_Compression._ad_CompressorIdLevelList, _0_Compression._tc_CompressorIdLevelList)
del CompressorIdLevelList

# typedef ... Buffer
class Buffer:
    _NP_RepositoryId = "IDL:omg.org/Compression/Buffer:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Compression.Buffer = Buffer
_0_Compression._d_Buffer  = omniORB.typeMapping["IDL:omg.org/CORBA/OctetSeq:1.0"]
_0_Compression._ad_Buffer = (omniORB.tcInternal.tv_alias, Buffer._NP_RepositoryId, "Buffer", omniORB.typeCodeMapping["IDL:omg.org/CORBA/OctetSeq:1.0"]._d)
_0_Compression._tc_Buffer = omniORB.tcInternal.createTypeCode(_0_Compression._ad_Buffer)
omniORB.registerType(Buffer._NP_RepositoryId, _0_Compression._ad_Buffer, _0_Compression._tc_Buffer)
del Buffer

# forward interface CompressorFactory;
_0_Compression._d_CompressorFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/Compression/CompressorFactory:1.0", "CompressorFactory")
omniORB.typeMapping["IDL:omg.org/Compression/CompressorFactory:1.0"] = _0_Compression._d_CompressorFactory

# interface Compressor
_0_Compression._d_Compressor = (omniORB.tcInternal.tv_objref, "IDL:omg.org/Compression/Compressor:1.0", "Compressor")
omniORB.typeMapping["IDL:omg.org/Compression/Compressor:1.0"] = _0_Compression._d_Compressor
_0_Compression.Compressor = omniORB.newEmptyClass()
class Compressor :
    _NP_RepositoryId = _0_Compression._d_Compressor[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Compression.Compressor = Compressor
_0_Compression._tc_Compressor = omniORB.tcInternal.createTypeCode(_0_Compression._d_Compressor)
omniORB.registerType(Compressor._NP_RepositoryId, _0_Compression._d_Compressor, _0_Compression._tc_Compressor)

# Compressor operations and attributes
Compressor._d_compress = ((omniORB.typeMapping["IDL:omg.org/Compression/Buffer:1.0"], omniORB.typeMapping["IDL:omg.org/Compression/Buffer:1.0"]), (omniORB.typeMapping["IDL:omg.org/Compression/Buffer:1.0"], ), {_0_Compression.CompressionException._NP_RepositoryId: _0_Compression._d_CompressionException})
Compressor._d_decompress = ((omniORB.typeMapping["IDL:omg.org/Compression/Buffer:1.0"], omniORB.typeMapping["IDL:omg.org/Compression/Buffer:1.0"]), (omniORB.typeMapping["IDL:omg.org/Compression/Buffer:1.0"], ), {_0_Compression.CompressionException._NP_RepositoryId: _0_Compression._d_CompressionException})
Compressor._d__get_compressor_factory = ((),(omniORB.typeMapping["IDL:omg.org/Compression/CompressorFactory:1.0"],),None)
Compressor._d__get_compression_level = ((),(omniORB.typeMapping["IDL:omg.org/Compression/CompressionLevel:1.0"],),None)
Compressor._d__get_compressed_bytes = ((),(omniORB.tcInternal.tv_ulonglong,),None)
Compressor._d__get_uncompressed_bytes = ((),(omniORB.tcInternal.tv_ulonglong,),None)
Compressor._d__get_compression_ratio = ((),(omniORB.typeMapping["IDL:omg.org/Compression/CompressionRatio:1.0"],),None)

# Compressor object reference
class _objref_Compressor (CORBA.Object):
    _NP_RepositoryId = Compressor._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def compress(self, *args):
        return self._obj.invoke("compress", _0_Compression.Compressor._d_compress, args)

    def decompress(self, *args):
        return self._obj.invoke("decompress", _0_Compression.Compressor._d_decompress, args)

    def _get_compressor_factory(self, *args):
        return self._obj.invoke("_get_compressor_factory", _0_Compression.Compressor._d__get_compressor_factory, args)

    compressor_factory = property(_get_compressor_factory)


    def _get_compression_level(self, *args):
        return self._obj.invoke("_get_compression_level", _0_Compression.Compressor._d__get_compression_level, args)

    compression_level = property(_get_compression_level)


    def _get_compressed_bytes(self, *args):
        return self._obj.invoke("_get_compressed_bytes", _0_Compression.Compressor._d__get_compressed_bytes, args)

    compressed_bytes = property(_get_compressed_bytes)


    def _get_uncompressed_bytes(self, *args):
        return self._obj.invoke("_get_uncompressed_bytes", _0_Compression.Compressor._d__get_uncompressed_bytes, args)

    uncompressed_bytes = property(_get_uncompressed_bytes)


    def _get_compression_ratio(self, *args):
        return self._obj.invoke("_get_compression_ratio", _0_Compression.Compressor._d__get_compression_ratio, args)

    compression_ratio = property(_get_compression_ratio)


omniORB.registerObjref(Compressor._NP_RepositoryId, _objref_Compressor)
_0_Compression._objref_Compressor = _objref_Compressor
del Compressor, _objref_Compressor

# Compressor skeleton
__name__ = "omniORB.Compression__POA"
class Compressor (PortableServer.Servant):
    _NP_RepositoryId = _0_Compression.Compressor._NP_RepositoryId


    _omni_op_d = {"compress": _0_Compression.Compressor._d_compress, "decompress": _0_Compression.Compressor._d_decompress, "_get_compressor_factory": _0_Compression.Compressor._d__get_compressor_factory, "_get_compression_level": _0_Compression.Compressor._d__get_compression_level, "_get_compressed_bytes": _0_Compression.Compressor._d__get_compressed_bytes, "_get_uncompressed_bytes": _0_Compression.Compressor._d__get_uncompressed_bytes, "_get_compression_ratio": _0_Compression.Compressor._d__get_compression_ratio}

Compressor._omni_skeleton = Compressor
_0_Compression__POA.Compressor = Compressor
omniORB.registerSkeleton(Compressor._NP_RepositoryId, Compressor)
del Compressor
__name__ = "omniORB.Compression"

# typedef ... CompressorSeq
class CompressorSeq:
    _NP_RepositoryId = "IDL:omg.org/Compression/CompressorSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Compression.CompressorSeq = CompressorSeq
_0_Compression._d_CompressorSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/Compression/Compressor:1.0"], 0)
_0_Compression._ad_CompressorSeq = (omniORB.tcInternal.tv_alias, CompressorSeq._NP_RepositoryId, "CompressorSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/Compression/Compressor:1.0"], 0))
_0_Compression._tc_CompressorSeq = omniORB.tcInternal.createTypeCode(_0_Compression._ad_CompressorSeq)
omniORB.registerType(CompressorSeq._NP_RepositoryId, _0_Compression._ad_CompressorSeq, _0_Compression._tc_CompressorSeq)
del CompressorSeq

# interface CompressorFactory
_0_Compression._d_CompressorFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/Compression/CompressorFactory:1.0", "CompressorFactory")
omniORB.typeMapping["IDL:omg.org/Compression/CompressorFactory:1.0"] = _0_Compression._d_CompressorFactory
_0_Compression.CompressorFactory = omniORB.newEmptyClass()
class CompressorFactory :
    _NP_RepositoryId = _0_Compression._d_CompressorFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Compression.CompressorFactory = CompressorFactory
_0_Compression._tc_CompressorFactory = omniORB.tcInternal.createTypeCode(_0_Compression._d_CompressorFactory)
omniORB.registerType(CompressorFactory._NP_RepositoryId, _0_Compression._d_CompressorFactory, _0_Compression._tc_CompressorFactory)

# CompressorFactory operations and attributes
CompressorFactory._d__get_compressor_id = ((),(omniORB.typeMapping["IDL:omg.org/Compression/CompressorId:1.0"],),None)
CompressorFactory._d_get_compressor = ((omniORB.typeMapping["IDL:omg.org/Compression/CompressionLevel:1.0"], ), (omniORB.typeMapping["IDL:omg.org/Compression/Compressor:1.0"], ), None)

# CompressorFactory object reference
class _objref_CompressorFactory (CORBA.Object):
    _NP_RepositoryId = CompressorFactory._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def _get_compressor_id(self, *args):
        return self._obj.invoke("_get_compressor_id", _0_Compression.CompressorFactory._d__get_compressor_id, args)

    compressor_id = property(_get_compressor_id)


    def get_compressor(self, *args):
        return self._obj.invoke("get_compressor", _0_Compression.CompressorFactory._d_get_compressor, args)

omniORB.registerObjref(CompressorFactory._NP_RepositoryId, _objref_CompressorFactory)
_0_Compression._objref_CompressorFactory = _objref_CompressorFactory
del CompressorFactory, _objref_CompressorFactory

# CompressorFactory skeleton
__name__ = "omniORB.Compression__POA"
class CompressorFactory (PortableServer.Servant):
    _NP_RepositoryId = _0_Compression.CompressorFactory._NP_RepositoryId


    _omni_op_d = {"_get_compressor_id": _0_Compression.CompressorFactory._d__get_compressor_id, "get_compressor": _0_Compression.CompressorFactory._d_get_compressor}

CompressorFactory._omni_skeleton = CompressorFactory
_0_Compression__POA.CompressorFactory = CompressorFactory
omniORB.registerSkeleton(CompressorFactory._NP_RepositoryId, CompressorFactory)
del CompressorFactory
__name__ = "omniORB.Compression"

# typedef ... CompressorFactorySeq
class CompressorFactorySeq:
    _NP_RepositoryId = "IDL:omg.org/Compression/CompressorFactorySeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_Compression.CompressorFactorySeq = CompressorFactorySeq
_0_Compression._d_CompressorFactorySeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/Compression/CompressorFactory:1.0"], 0)
_0_Compression._ad_CompressorFactorySeq = (omniORB.tcInternal.tv_alias, CompressorFactorySeq._NP_RepositoryId, "CompressorFactorySeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/Compression/CompressorFactory:1.0"], 0))
_0_Compression._tc_CompressorFactorySeq = omniORB.tcInternal.createTypeCode(_0_Compression._ad_CompressorFactorySeq)
omniORB.registerType(CompressorFactorySeq._NP_RepositoryId, _0_Compression._ad_CompressorFactorySeq, _0_Compression._tc_CompressorFactorySeq)
del CompressorFactorySeq

# interface CompressionManager
_0_Compression._d_CompressionManager = (omniORB.tcInternal.tv_objref, "IDL:omg.org/Compression/CompressionManager:1.0", "CompressionManager")
omniORB.typeMapping["IDL:omg.org/Compression/CompressionManager:1.0"] = _0_Compression._d_CompressionManager
_0_Compression.CompressionManager = omniORB.newEmptyClass()
class CompressionManager :
    _NP_RepositoryId = _0_Compression._d_CompressionManager[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Compression.CompressionManager = CompressionManager
_0_Compression._tc_CompressionManager = omniORB.tcInternal.createTypeCode(_0_Compression._d_CompressionManager)
omniORB.registerType(CompressionManager._NP_RepositoryId, _0_Compression._d_CompressionManager, _0_Compression._tc_CompressionManager)

# CompressionManager operations and attributes
CompressionManager._d_register_factory = ((omniORB.typeMapping["IDL:omg.org/Compression/CompressorFactory:1.0"], ), (), {_0_Compression.FactoryAlreadyRegistered._NP_RepositoryId: _0_Compression._d_FactoryAlreadyRegistered})
CompressionManager._d_unregister_factory = ((omniORB.typeMapping["IDL:omg.org/Compression/CompressorId:1.0"], ), (), {_0_Compression.UnknownCompressorId._NP_RepositoryId: _0_Compression._d_UnknownCompressorId})
CompressionManager._d_get_factory = ((omniORB.typeMapping["IDL:omg.org/Compression/CompressorId:1.0"], ), (omniORB.typeMapping["IDL:omg.org/Compression/CompressorFactory:1.0"], ), {_0_Compression.UnknownCompressorId._NP_RepositoryId: _0_Compression._d_UnknownCompressorId})
CompressionManager._d_get_compressor = ((omniORB.typeMapping["IDL:omg.org/Compression/CompressorId:1.0"], omniORB.typeMapping["IDL:omg.org/Compression/CompressionLevel:1.0"]), (omniORB.typeMapping["IDL:omg.org/Compression/Compressor:1.0"], ), {_0_Compression.UnknownCompressorId._NP_RepositoryId: _0_Compression._d_UnknownCompressorId})
CompressionManager._d_get_factories = ((), (omniORB.typeMapping["IDL:omg.org/Compression/CompressorFactorySeq:1.0"], ), None)

# CompressionManager object reference
class _objref_CompressionManager (CORBA.Object):
    _NP_RepositoryId = CompressionManager._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def register_factory(self, *args):
        return self._obj.invoke("register_factory", _0_Compression.CompressionManager._d_register_factory, args)

    def unregister_factory(self, *args):
        return self._obj.invoke("unregister_factory", _0_Compression.CompressionManager._d_unregister_factory, args)

    def get_factory(self, *args):
        return self._obj.invoke("get_factory", _0_Compression.CompressionManager._d_get_factory, args)

    def get_compressor(self, *args):
        return self._obj.invoke("get_compressor", _0_Compression.CompressionManager._d_get_compressor, args)

    def get_factories(self, *args):
        return self._obj.invoke("get_factories", _0_Compression.CompressionManager._d_get_factories, args)

omniORB.registerObjref(CompressionManager._NP_RepositoryId, _objref_CompressionManager)
_0_Compression._objref_CompressionManager = _objref_CompressionManager
del CompressionManager, _objref_CompressionManager

# CompressionManager skeleton
__name__ = "omniORB.Compression__POA"
class CompressionManager (PortableServer.Servant):
    _NP_RepositoryId = _0_Compression.CompressionManager._NP_RepositoryId


    _omni_op_d = {"register_factory": _0_Compression.CompressionManager._d_register_factory, "unregister_factory": _0_Compression.CompressionManager._d_unregister_factory, "get_factory": _0_Compression.CompressionManager._d_get_factory, "get_compressor": _0_Compression.CompressionManager._d_get_compressor, "get_factories": _0_Compression.CompressionManager._d_get_factories}

CompressionManager._omni_skeleton = CompressionManager
_0_Compression__POA.CompressionManager = CompressionManager
omniORB.registerSkeleton(CompressionManager._NP_RepositoryId, CompressionManager)
del CompressionManager
__name__ = "omniORB.Compression"

#
# End of module "Compression"
#
__name__ = "compression_idl"

_exported_modules = ( "omniORB.Compression", )

# The end.