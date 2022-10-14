import tkinter as tk

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

janela = tk.Tk()
janela.title('Cronometro') # Nome do software
janela.geometry('370x200')
janela.resizable(width=False, height=False)
janela.configure(background=cor1)
#janela.iconphoto(False, tk.PhotoImage(file='yo')) # icone do software


global tempo
tempo = '00:00:00'

count = -5
run = False


# Funcao iniciar
def iniciar():
   def valor():
      if run:
         global count
         global tempo
         # antes de comecar
         if count <= -1:
            inicio = "começando em " + str(abs(count))
            label_time['text'] = inicio
            label_time['font'] =  'ivy 20 '
         else:
             label_time['font'] =  'Times 50 bold'
             d = str(tempo)
             h,m,s = map(int,d.split(":")) 
             h = int(h)
             m=int(m)
             s= int(count)
                 
             if(s>=5):
                 count = 0
                 m+=1
              
             s=str(0)+str(s)
             m=str(0)+str(m)
             h=str(0)+str(h)
                
             d=str(h[-2:])+":"+str(m[-2:])+":"+str(s[-2:])
             label_time['text'] = d
             tempo = d
            
             s= int(count)
             m= int(m)
             h= int(h)             
         
         label_time.after(1000, valor)
         count += 1
   valor()
   
# Funcao para iniciar
def start():
   global run
   run = True
   iniciar()
   
# Funacao para pausar
def stop():
   global run
   run = False

# funcao para reiniciar
def reset():
   global count
   count = -5
   
   # Se estiver pausado ira reiniciar do zero
   if run == False:
       global tempo
       tempo = '00:00:00'
       label_time['text'] = tempo

   # Se nao estiver pausado ira continuar onde parou antes 
   else:
      label_time['font'] =  'ivy 20 '
      label_time['text'] = 'Iniciando...'


label_app = tk.Label(janela, text='© 2022 Ramon S Antonio', font=('Arial 10'), bg=cor1, fg='white')
label_app.place(x=110,y=85)

label_time = tk.Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg='green')
label_time.grid(row=0, column=0, sticky=tk.NSEW, padx=15, pady=20)

label_app.lift()

frameBaixo = tk.Frame(janela,width=310, height=350,bg=cor1, relief="flat")
frameBaixo.grid(row=1, column=0,pady=0, padx=30, sticky=tk.NSEW)

botao_start = tk.Button(frameBaixo,command=start, text="Iniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief=tk.RAISED, overrelief=tk.RIDGE)
botao_start.grid(row=0, column=0, sticky=tk.NSEW, padx=2, pady=10)

botao_stop = tk.Button(frameBaixo,command=stop, text="Pausar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief=tk.RAISED, overrelief=tk.RIDGE)
botao_stop.grid(row=0, column=1, sticky=tk.NSEW, padx=2, pady=10)

botao_reset = tk.Button(frameBaixo, command=reset, text="Reiniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief=tk.RAISED, overrelief=tk.RIDGE)
botao_reset.grid(row=0, column=2, sticky=tk.NSEW, padx=2, pady=10)


janela.mainloop()