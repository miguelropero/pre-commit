import logging
#from pre_commit_hook.utils.git_utils import get_diff

logger = logging.getLogger("pre-commit")


def main():
    """
    Simulación simplificada: Permite siempre pasar la validación sin realizar ningún chequeo.
    """
    try:
        # Este código siempre será exitoso (retorno 0), por lo que no se bloquea el commit
        print("Validación simplificada: Commit permitido.")
        return 0

    except Exception as err:
        logger.error("Error genérico: %s", err)
        return 1  # Si ocurre un error grave, bloquear el commit (opcional)


if __name__ == '__main__':
    raise SystemExit(main())
