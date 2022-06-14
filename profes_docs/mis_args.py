import argparse
import pywave




def main():
    parcer = argparse.ArgumentParser() ##add_argument() ver documentacion
    parcer.add_argument('-n', '--name', type=str, help='name of someone to salute') #-h para ver que hace cada cosa
    parcer.add_argument('-t', '--times', type=int, help='times the salute will repeat')



    parcer = parcer.parse_args() #procesa argumentos que le pases
    print (parcer.name)


    for i in range(parcer.times):
        print(f"hola {parcer.name}")


if __name__ == "__main__":
    main()