from wand.image import Image, COMPOSITE_OPERATORS
from wand.drawing import Drawing
from wand.color import Color
from wand.compat import nested

print("Bem vindo ao gerador de fichas gensou!")
bonecos = ["suika", "yukari", "yuyuko", "remilia", "youmu", "patchouli", "alice", "sakuya", "marisa", "reimu", "sanae",
           "cirno", "meiling", "okuu", "suwako", "reisen", "aya", "komachi", "iku", "tenshi"]
"""
Gerador de fichas gensou versão 0.número
O programa era tão simples que nem precisava de classe
Basicamente, você coloca o personagem e pronto

"""
# Pequeno guia de como usar
# Os valores de x e y contam como (0,0) o local no canto
# superior esquerdo, e de lá crescem
# não há métodos para customizar texto, infelizmente
# eu não sei programar



def char_select():
    """
    Essa função escolhe o fundo da personagem
    Tanto faz se escreve sUIkA ou suika ou SUIKA
    mas por exemplo, em okuu não é válido utsuho
    dá pra implementar mas isso é um saco, faço quando for fazer a UI
    """
    sovai = False
    while not sovai:
        if boneca in bonecos:
            print("A Main é {}".format(boneca.capitalize()))
            with Image(filename="bonecas/{}.png".format(boneca.lower())) as img:
                with img.clone() as i:
                    i.save(filename='nova{}.png'.format(boneca.lower()))
                    sovai = True
        else:
            print("Tá errado nego")
            sovai = False


def name_select():
    """
    Como a função sugere essa função desenha o nome da pessoa.
    Tem um macete para dropshadow, que também é usado na função de localizaçõo
    não tem mais o que explicar, não sei se é possível fazer em apenas um
    Drawing(), provavelmente é mas o programa funciona do jeito que tá
    """
    dimensions = {'width': 420,
                  'height': 150}
    with nested(Image(filename='nova{}.png'.format(boneca.lower())),
                Image(background=Color('transparent'), **dimensions)) as (img, shadow):
        with Drawing() as ctx:
            ctx.font = 'verdanab.ttf'
            ctx.fill_color = "black"
            ctx.text_alignment = 'center'
            ctx.font_size = 27.57
            ctx.text(210, 31, '{}'.format(name))
            ctx(shadow)
        shadow.gaussian_blur(8, 8)
        with Drawing() as draw:
            draw.font = 'verdanab.ttf'
            draw.fill_color = "rgb(255, 255, 255)"
            draw.font_size = 27.57
            draw.text_alignment = 'center'
            draw.stroke_opacity = 78
            draw.text(210, 33, '{}'.format(name))
            draw(shadow)
        img.composite(shadow, 0, 0)
        img.save(filename='ficha {}.png'.format(name))


def local_select():
    """
    Mesma coisa da função acima, para local no entanto
    """
    dimensions = {'width': 420, 'height': 150}
    with nested(Image(filename='ficha {}.png'.format(name)),
                Image(background=Color('transparent'), **dimensions)) as (img, shadow):
        with Drawing() as ctx:
            ctx.font = 'framd.ttf'
            ctx.fill_color = "black"
            ctx.font_size = 11.97
            ctx.text(34, 111, '{}'.format(local))
            ctx(shadow)
        shadow.gaussian_blur(1, 1)
        with Drawing() as draw:
            draw.font = 'framd.ttf'
            draw.fill_color = "rgb(255, 255, 255)"
            draw.font_size = 11.97
            draw.text(35, 111, '{}'.format(local))
            draw(shadow)
        img.composite(shadow, 0, 0)
        img.save(filename='ficha {}.png'.format(name))
B f

def photo_select():
    """
    FUNÇÃO TEMPORÁRIA
    IMPLEMENTAR CAIXA DE TEXTO NA UI
    Você digita o nome do arquivo da imagem
    (tem que estar na root de onde você rodar o programa)
    """
    for _ in COMPOSITE_OPERATORS:
        ficha = Image(filename="ficha {}.png".format(name))
        foto = Image(filename="{}".format(pfp))
        with Drawing() as draw:
            draw.composite(operator='over', left=22, top=32, width=60, height=60, image=foto)
            draw(ficha)
            ficha.save(filename="ficha {}.png".format(name))
    print(pfp)


def attr_select():
    """
    FUNÇÃO TEMPORÁRIA
    IMPLEMENTAR CAIXA DE TEXTO NA UI
    Escolha dos atributos acima
    """
    for _ in COMPOSITE_OPERATORS:
        ficha = Image(filename="ficha {}.png".format(name))
        atr = Image(filename="cartas/{}.png".format(atributo))
        atr.transparent_color(color=Color('black'), alpha=0.2)
        with Drawing() as draw:
            draw.composite(operator='over', left=0, top=0, width=atr.width, height=atr.height, image=atr)
            draw(ficha)
            ficha.save(filename="ficha {}.png".format(name))
    print(atributo)


boneca = input("Digite aqui a main: ").lower()
char_select()
name = input("\nDigite aqui seu nome: ")
name_select()
local = input("\nDigite aqui seu local: ")
local_select()
pfp = input("\nDigite aqui o nome do arquivo da foto COM a extensão: ")
print("O aplicativo tem suporte a PNG, JPG, JPEG, GIF e BMP")
photo_select()
atributo = input("\nDigite aqui os atributos da ficha: "
                 "\nPor motivos de preguiça apenas 1 é suportado no momento ").lower()
attr_select()
