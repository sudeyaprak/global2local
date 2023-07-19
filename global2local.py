xr = float(input("X coordinate's of observation point:"))
yr = float(input("Y coordinate's of observation point:"))
zr = float(input("Z coordinate's of observation point:"))

xp = float(input("X coordinate's of target point:"))
yp = float(input("X coordinate's of target point:"))
zp = float(input("X coordinate's of target point:"))

import math
import numpy as np

def global2local(xp,yp,zp,xr,yr,zr):
    
    S2 = [[1, 0, 0],
          [0, -1, 0],
          [0, 0, 1]]
    
    deltax = [[xp-xr],
              [yp-yr],
              [zp-zr]]
    
    #finding φ and λ
    def xyz2blh(xr,yr,zr):
    
        #Parameters of GRS80 ellipsoid
        a = 6378137.0
        b = 6356752.3141 
     
        #Eccentricity
        e = math.sqrt(1-(b**2)/(a**2))
  
        #Longitude
        λ = math.atan2(yr, xr)
  
        #Latitude
        h0 = 0
        φ = math.atan((zr / math.sqrt(xr**2+yr**2))*((1-e**2)**(-1)))
  
        while abs(φ - h0) > 10**(-12):
            h0 = φ
            N = a / math.sqrt(1 - e**2 * math.sin(h0)**2)
            φ = math.atan((zr / math.sqrt(xr**2+yr**2))*((1 - (e**2 * N)/(N +h0))**(-1)))
    
        return λ, φ

    λ, φ = xyz2blh(xr,yr,zr)
    np.radians(λ)
    np.radians(φ)
    
    R2 =  [[np.cos(φ-1.5708), 0, -np.sin(φ-1.5708)], 
           [0, 1, 0], 
           [np.sin(φ-1.5708), 0 ,np.cos(φ-1.5708)]]
   
    R3 = [[np.cos(λ-3.14159), np.sin(λ-3.14159), 0], 
          [-np.sin(λ-3.14159), np.cos(λ-3.14159), 0], 
          [0, 0, 1]]
    
    dxe = np.dot(np.dot(np.dot(S2,R2),R3),deltax)
    xe, ye, ze = dxe[0],dxe[1],dxe[2]
    
    azimuth = np.arctan2(ye,xe)
    zenith = np.arctan2(ye, ze*np.sin(azimuth))
    r = np.sqrt(xe**2+ye**2+ze**2)
    
    return np.degrees(azimuth), np.degrees(zenith), r
    
print(global2local(xp,yp,zp,xr,yr,zr))
