# Olá! Eu sou Lucas Dal Pra 👋

Bem-vindo ao meu perfil do GitHub! Eu utilizo ele como um portifolio pessoal para todos os meus projetos. Os mais importantes estão todos com uma documentação completa.

![image](https://github.com/user-attachments/assets/12bff718-0e5a-4a02-bbd0-95920b783d62)

---
![github-user-contribution](https://github.com/user-attachments/assets/d7404fed-6fc9-47d4-9b46-5027c0303bab)

[Uplo<!DOCTYPE html>
<html lang="en"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <meta charset="UTF-8">
  

    <link rel="apple-touch-icon" type="image/png" href="https://cpwebassets.codepen.io/assets/favicon/apple-touch-icon-5ae1a0698dcc2402e9712f7d01ed509a57814f994c660df9f7a952f3060705ee.png">

    <meta name="apple-mobile-web-app-title" content="CodePen">

    <link rel="icon" type="image/x-icon" href="https://cpwebassets.codepen.io/assets/favicon/favicon-aec34940fbc1a6e787974dcd360f2c6b63348d4b1f4e06c77743096d55480f33.ico">

    <link rel="mask-icon" type="image/x-icon" href="https://cpwebassets.codepen.io/assets/favicon/logo-pin-b4b4269c16397ad2f0f7a01bcdf513a1994f4c94b8af2f191c09eb0d601762b1.svg" color="#111">



  
  

  <title>Pac-Man in pure SVG</title>

    <link rel="canonical" href="https://codepen.io/nshew/pen/WNvGKLY">
  
  
  
  
<style>
.pacman-container {
  background-color: darkblue;
  /* Use calc to maintain aspect ratio when scaling. */
  height: calc(300px/2);
  width: calc(600px/2);
}
</style>

  <script>
  window.console = window.console || function(t) {};
</script>

  
  
</head>

<body translate="no">
  



  <meta charset="UTF-8">
  <title>SVG Pac-Man</title>



  <div class="pacman-container">
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" class="pacman" viewBox="0 0 600 300">
      <!-- In order to externalize the SVG for use as an object, we have to put all the necessary styling inline here. -->
      <style>
        .pacman-dot {
          fill: white;
        }

        .pacman-open,
        .pacman-mouth-top,
        .pacman-mouth-bottom {
          fill: gold;
        }

        .pacman-mouth-top,
        .pacman-mouth-bottom {
          animation-duration: 175ms;
          animation-timing-function: linear;
          animation-direction: alternate;
          animation-iteration-count: infinite;
          transform-origin: calc(300px/2) 150px; // center of circle
        }

        .pacman-mouth-top {
          animation-name: rotate-counterclockwise;
        }

        .pacman-mouth-bottom {
          animation-name: rotate-clockwise;
        }

        @keyframes rotate-counterclockwise {
          100% {
            transform: rotate(-30deg);
          }
        }

        @keyframes rotate-clockwise {
          100% {
            transform: rotate(30deg);
          }
        }


        .pacman-dot {
          animation-name: dot-motion;
          animation-duration: 600ms;
          animation-timing-function: linear;
          animation-iteration-count: infinite;
        }

        @keyframes dot-motion {
          100% {
            transform: translateX(-100px); // distance between dots
          }
        }
      </style>
      <circle class="pacman-dot" cx="250" cy="50%" r="10"></circle>
      <circle class="pacman-dot" cx="350" cy="50%" r="10"></circle>
      <circle class="pacman-dot" cx="450" cy="50%" r="10"></circle>
      <circle class="pacman-dot" cx="550" cy="50%" r="10"></circle>
      <circle class="pacman-dot" cx="650" cy="50%" r="10"></circle>
      <!-- Create arcs covering 45°, so there's a little overlap with animations of 30°. -->
      <path class="pacman-mouth-bottom" d="
        M 150,150
        L 220.4,221.0
        A 100 100 0 0 0 250,150
        Z"></path>
      <path class="pacman-mouth-top" d="
        M 150,150 
        L 220.4,79.0
        A 100 100 0 0 1 250,150
        Z"></path>
      <path class="pacman-open" d="
        M 150,150
        L 236.6,100
        A 100 100 0 1 0 236.6,200
        Z"></path>
    </svg>

  </div>


  
  
  



</body></html>ading Pac-Man in pure SVG.html…]()

---

## 🌐 Socials:
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/dalpra0) 

# 💻 Tech Stack:
![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white) ![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white) ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white) ![Objective-C](https://img.shields.io/badge/OBJECTIVE--C-%233A95E3.svg?style=for-the-badge&logo=apple&logoColor=white) ![Perl](https://img.shields.io/badge/perl-%2339457E.svg?style=for-the-badge&logo=perl&logoColor=white) ![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white) ![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white) ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white) ![Swift](https://img.shields.io/badge/swift-F54A2A?style=for-the-badge&logo=swift&logoColor=white) ![Bash Script](https://img.shields.io/badge/bash_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![OpenGL](https://img.shields.io/badge/OpenGL-%23FFFFFF.svg?style=for-the-badge&logo=opengl) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white) ![Adobe](https://img.shields.io/badge/adobe-%23FF0000.svg?style=for-the-badge&logo=adobe&logoColor=white) ![Adobe Lightroom](https://img.shields.io/badge/Adobe%20Lightroom-31A8FF.svg?style=for-the-badge&logo=Adobe%20Lightroom&logoColor=white) ![Adobe Lightroom Classic](https://img.shields.io/badge/Adobe%20Lightroom%20Classic-31A8FF.svg?style=for-the-badge&logo=Adobe%20Lightroom%20Classic&logoColor=white) ![Adobe Photoshop](https://img.shields.io/badge/adobe%20photoshop-%2331A8FF.svg?style=for-the-badge&logo=adobe%20photoshop&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white) ![Raspberry Pi](https://img.shields.io/badge/-Raspberry_Pi-C51A4A?style=for-the-badge&logo=Raspberry-Pi) ![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white) ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white) ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white) ![Aseprite](https://img.shields.io/badge/Aseprite-FFFFFF?style=for-the-badge&logo=Aseprite&logoColor=#7D929E) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![Cisco](https://img.shields.io/badge/cisco-%23049fd9.svg?style=for-the-badge&logo=cisco&logoColor=black)
# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=DalPra0&theme=dark&hide_border=false&include_all_commits=true&count_private=true)
![](https://nirzak-streak-stats.vercel.app/?user=DalPra0&theme=dark&hide_border=false)
![](https://github-readme-stats.vercel.app/api/top-langs/?username=DalPra0&theme=dark&hide_border=false&include_all_commits=true&count_private=true&layout=compact)
> **Nota:** Estes gráficos são atualizados automaticamente para refletir as quantidades e linguagens dos meus projetos.


## 🏆 GitHub Trophies
![](https://github-profile-trophy.vercel.app/?username=DalPra0&theme=radical&no-frame=false&no-bg=true&margin-w=4)

### ✍️ Random Dev Quote
![](https://quotes-github-readme.vercel.app/api?type=vertical&theme=dark)

### 🔝 Top Contributed Repo
![](https://github-contributor-stats.vercel.app/api?username=DalPra0&limit=5&theme=dark&combine_all_yearly_contributions=true)

---
[![](https://visitcount.itsvg.in/api?id=DalPra0&icon=0&color=13)](https://visitcount.itsvg.in)

## 🗓 Ultimo Projeto Finalizado

Esse é o ultimo projeto que trabalhei e finalizei"

- **[Hello, DalPra](https://github.com/DalPra0/Hello-DalPra)**: Este foi o meu primeiro trabalho com programação em swift, desde que entrei na academy

---

## ⭐ Principais Projetos

Aqui estão alguns dos projetos em que tenho trabalhado recentemente e que melhor demonstram minhas habilidades:

- [**SpellBound**](https://github.com/DalPra0/Spellbound) – Uma interface para jogar Magic the Gathering online com seus amigos, jogando com cartas reais. Contem aplicação de IA para analizar cartas e decks.
- [**Hello, DalPra**](https://github.com/DalPra0/Hello-DalPra) – Um jogo de ritmo feito na apple developer academy.
- [**Teste de Velocidade de Criptografia**](https://github.com/DalPra0/TesteVelocidadeCriptografia) – Projeto para a materia de Segurança da informação, feito para testar a velocidade de diferentes criptografias de dados.
- [**Watch Guard**](https://github.com/DalPra0/WatchGuard) - O projeto final da materia de Performance em Sistemas Cyberfisicos.

---

## 🚀 Meus Grandes Projetos

- **[RioAlerta](https://github.com/DalPra0/RioAlerta)**: Um projeto vencedor que conquistou o primeiro lugar na categoria Assistência Ambiental e Social no OBT 2023. Criado para monitoramento ambiental, desenvolvido em appinventor.mit.edu.


- **[Sistema Operacional](https://github.com/DalPra0/MontandoUmSistemaOperacional)**: Esse projeto eu estou aprendendo a como montar um sistema operacional. Eu quero programar um do zero e um a partir de linux.

---

## 📒 Meus estudos

Aqui deixo um repositorio meu onde estou organizando meus estudos, eu estou me aprofundando em algumas linguagens de programação, e aprendendo certas bibliotecas.

- **[Estudos](https://github.com/DalPra0/aprendendo)**: Não tem muito conteudo postado, eu apenas pretendo usar o readme.md e organizar pastas para fazer upload de documentos e pdf's sobre os conteudos.
- **[Livros](https://github.com/DalPra0/MontandoUmSistemaOperacional/tree/main/Livros)**: Um compilado de todos os livros que estou lendo ou que ja li.
