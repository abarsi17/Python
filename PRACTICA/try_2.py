try:
    raise NameError("Mi texto...")
except NameError as err:
    print("Error de nombre: %s " % err)
    raise