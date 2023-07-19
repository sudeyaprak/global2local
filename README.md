# global2local (xp, yp, zp, xr, yr, zr)

1. Inputs:
The `global2local` function takes six arguments representing the coordinates of two points:

- `xp`, `yp`, `zp`: The X, Y, and Z coordinates of the target point (point of interest) in a global coordinate system.
- `xr`, `yr`, `zr`: The X, Y, and Z coordinates of the observation point (reference point) in the same global coordinate system.

2. Purpose:
The primary purpose of the `global2local` function is to perform coordinate transformations from a global coordinate system (defined by the observation point) to a local coordinate system (defined by the target point). The function computes the azimuth, zenith angle, and distance (r) from the observation point to the target point in the local coordinate system.

3. Coordinate Transformation:
The function performs a series of coordinate transformations using rotation matrices. The transformation involves the following steps:

- Convert Global Coordinates to Ellipsoidal Latitude and Longitude:
The function converts the observation point's global XYZ coordinates (xr, yr, zr) to ellipsoidal latitude (φ) and longitude (λ) using the GRS80 ellipsoid parameters. This conversion involves iterative calculations to find the latitude (φ) that satisfies the relation between ellipsoidal height (h0) and the computed height (zr) above the ellipsoid surface.

- Rotate to the Local Tangent Plane:
The function creates a transformation matrix S2 that rotates the global XYZ coordinates to a local tangent plane with its Z-axis aligned with the normal to the ellipsoid at the observation point.

- Rotate to the Local North-East-Down (NED) System:
The function creates rotation matrices R2 and R3 to rotate the tangent plane coordinates (ξ, η, ζ) to a North-East-Down (NED) system. The NED system is a local coordinate system with its origin at the observation point, X-axis pointing north, Y-axis pointing east, and Z-axis pointing down.

- Compute Local Coordinates and Distance:
The function computes the difference in X, Y, and Z coordinates (deltax) between the target point and the observation point. It then transforms these differences to the local NED coordinate system (ξ, η, ζ) using the rotation matrices.

- Calculate Azimuth, Zenith Angle, and Distance:
Using the transformed local coordinates (ξ, η, ζ), the function calculates the azimuth and zenith angle (elevation angle) of the target point with respect to the observation point. The azimuth is the angle between the local north direction and the target point, while the zenith angle is the angle between the vertical direction (zenith) and the target point. The distance (r) from the observation point to the target point is also computed.

4. Return Values:
The function returns three values:

- Azimuth (in degrees) of the target point with respect to the observation point.
- Zenith angle (in degrees) of the target point with respect to the observation point.
- Distance (r) from the observation point to the target point in the local coordinate system.

5. Usage:
The function is used to convert global XYZ coordinates to a local NED coordinate system centered at the observation point. It provides important information about the direction and distance to the target point from the observation point in the local context.

Please note that the provided function depends on accurate and well-defined parameters for the ellipsoid (GRS80) and may require further validation and testing in real-world applications. Additionally, the function is missing a part that converts the angles from radians to degrees when returning the azimuth and zenith values, which could be included by wrapping `np.degrees()` around those values before returning them.
