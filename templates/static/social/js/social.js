var elemento = document.getElementById("perfil-imagem-capa")

if (post.perfil.imagem_capa) {
    elemento.classList.add("perfil-imagem-capa");
    log("perfil com capa")
  } else {
    elemento.classList.add("perfil-imagem-sem-capa");
  }