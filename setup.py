#!/usr/bin/env python

from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(
        name='synthesizer',
        version='1.0.0',
        license='MIT',
        authors='Mateo López Vilaclara, Fausto Julián Pettinari, Pedro Santiago Gentil',
        authors_mails='mlopezvilaclara@udesa.edu.ar, fpettinari@udesa.edu.ar, pgentil@udesa.edu.ar',
        packages= find_packages(
            where='.',
            exclude=['xylophone*']
        ),
        project_urls={ 
        "TP4": "https://github.com/pgentil/TP4/tree/main",
        }
    
    )