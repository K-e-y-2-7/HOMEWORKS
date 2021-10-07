def intexam (inp: str) -> int:
        inp = str(inp)
        while True:
            if inp.isdigit() == 1:
                inp = int(inp)
                break
            else:
                inp = str(input('Ввод не integer. Повторите ввод: '))
        return inp

def floatexam (inp: str) -> float:
        inp = str(inp)
        while True:
            if inp.replace(".", "", 1).isdigit() == 1:
                inp = float(inp)
                break
            else:
                inp = str(input('Ввод не float. Повторите ввод: '))
        return inp