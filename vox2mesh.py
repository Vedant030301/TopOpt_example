import numpy as np
from skimage import measure
import meshio

# Load flat voxel array
voxels = np.load('voxel_output.npy')
print("Original shape:", voxels.shape)

# Reshape to 2D and then stack to make it 3D
voxels = voxels.reshape((90, 30))  # reshape to 2D
voxels = np.stack([voxels, voxels], axis=10)  # make it 3D: (90, 30, 2)
print("After stacking:", voxels.shape)

# Threshold
voxels = voxels > 0.5

# Generate mesh
verts, faces, normals, values = measure.marching_cubes(voxels, level=0)

# Save as STL
mesh = meshio.Mesh(points=verts, cells=[("triangle", faces)])
mesh.write("output.stl")
