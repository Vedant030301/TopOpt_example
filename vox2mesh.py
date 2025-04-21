import numpy as np
from skimage import measure
import meshio

# Step 1: Load flat voxel array (1D with 2700 elements)
voxels = np.load('voxel_output.npy')
print("Original shape:", voxels.shape)  # should be (2700,)

# Step 2: Reshape to 2D (90 x 30), then stack to make 3D volume (depth = 10)
voxels = voxels.reshape((90, 30))
voxels = np.stack([voxels] * 10, axis=2)  # final shape: (90, 30, 10)
print("Reshaped to:", voxels.shape)

# Step 3: Convert to binary using threshold
voxels = voxels > 0.5

# Step 4: Generate mesh using marching cubes
verts, faces, normals, values = measure.marching_cubes(voxels, level=0)

# Step 5: Write mesh to STL file
mesh = meshio.Mesh(points=verts, cells=[("triangle", faces)])
mesh.write("output.stl")

print("✅ STL file 'output.stl' generated successfully.")
