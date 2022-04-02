import patoolib


def unrar(filepath, outdir):
    print("Unrar data {}".format(filepath))

    patoolib.extract_archive(filepath, outdir=outdir)
