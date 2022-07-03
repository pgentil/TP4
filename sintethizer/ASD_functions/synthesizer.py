# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 15:40:00 2022

@author: HP
"""

from scipy.io.wavfile import write

sample_rate = 44100
def create_song(archive_name, sample_rate, array_song):
    """
    Creates a wavefile
    Parameters
    ----------
    archive_name : String
        The archive's name.
    sample_rate : Int
        Generally 44100.
    array_song : Array
        Array which contains the functions values.

    """
    write(archive_name, sample_rate, array_song)
    