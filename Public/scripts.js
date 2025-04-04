document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  // Simula um login básico. Depois isso será substituído por backend real.
  if (email === "teste@teste.com" && password === "123456") {
    alert("Login bem-sucedido!");
    window.location.href = "upload.html"; // Página de upload será criada depois
  } else {
    alert("Credenciais inválidas. Tente novamente.");
  }
});
