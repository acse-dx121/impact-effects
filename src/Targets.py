from src.config import *


class Target:

    def __init__(self, rhoSurface=1, dragC=2, schaleHeight=8000,
                 fp=7, pEarth=1.794 * 10 ** 32, mEarth=5.97 * 10 ** 24,
                 lEarth=5.86 * 10 ** 33, g=9.8, R_earth=6370, surface_wave_v=5,
                 melt_coeff=8.9 * 10 ** -21, vEarth=1.1 * 10 ** 12):
        
        self.rhoSurface = rhoSurface  # suface density of atmosphere kg/m^3
        self.dragC = dragC
        self.fp = fp
        self.schaleHeight = schaleHeight
        self.pEarth = pEarth
        self.mEarth = mEarth
        self.lEarth = lEarth
        self.g = g
        self.R_earth = R_earth
        self.surface_wave_v = surface_wave_v
        self.melt_coeff = melt_coeff
        self.vEarth = vEarth

        return

    def get_rhoSurface(self):
        return self.rhoSurface
    
    def get_dragC(self):
        return self.dragC
    
    def get_schaleHeight(self):
        return self.schaleHeight
    
    def get_fp(self):
        return self.fp
    
    def get_pEarth(self):
        return self.pEarth
    
    def get_mEarth(self):
        return self.mEarth
    
    def get_lEarth(self):
        return self.lEarth
    
    def get_g(self):
        return self.g
    
    def get_R_earth(self):
        return self.R_earth
    
    def get_surface_wave_v(self):
        return self.surface_wave_v
    
    def get_melt_coeff(self):
        return self.melt_coeff
    
    def get_v_earth(self):
        return self.vEarth