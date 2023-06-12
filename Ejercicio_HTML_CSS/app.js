
var libro = {
    titulo: 'Las Legiones Malditas',
    autor: 'Santiago Posterguillo',
    informacion:function () { return this.titulo + " escrito por " + this.autor;}
    }

    console.log(typeof libro.informacion)

    let intentos = [1, 5, 10, 12]
    console.log(intentos[4])

    let siglas = [
        'FMI',
        'BID',
        ['ONU', 'UNESCO'],
        'BIRF'
    ]

    console.log(siglas[2][1]);

    let numeros = [5, 5, [3, 4, [5, 6], 7]]
    console.log(numeros[2][2][1])

    let paises = [['MX', 'CA'], 'ES']
    console.log(paises[0][0][0]);