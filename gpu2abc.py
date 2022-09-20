import maya.cmds as mc

# Get selected leaf shapes (so we can filter to gpuCaches)
selShapes = mc.ls(sl=1, dag=1, leaf=1, shapes=1, long=True)

# Filter to gpuCache (doesn't work as one-liner above)
gpuCacheShapes = mc.ls(selShapes, long=True, type='gpuCache')

for gpuCacheShape in gpuCacheShapes:
    transform = mc.listRelatives(gpuCacheShape, parent=True, fullPath=True)[0]
    filepath = mc.getAttr(gpuCacheShape + '.cacheFileName')
   
    # Import everything from filepath and reparent under the transform
    mc.AbcImport(filepath, mode="import", reparent=transform)
   
    # Hide the original gpuCache shape?
    mc.setAttr(gpuCacheShape + '.visibility', 0)
   
    #(Or delete it?)
    #mc.delete(gpuCacheShape)