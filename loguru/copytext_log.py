from loguru import logger
import subprocess

def copy(file_path1,file_path2):
    try:
        subprocess.run(f"cp {file_path1} {file_path2}")
        logger.debug(f"Copy text from{file_path1} to {file_path2}")
        logger.info(f"Func(copy) done!")
    except:
        logger.error("!Error! func(copy) dont work !Error!")

file_path1 = str(input("Enter file_path source: "))
file_path2 = str(input("Enter file_path final: "))

copy(file_path1,file_path2)