<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Média por Bairro</title>
	<!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

</head>
<body>
	<div class="container-fluid" style="background-image: url(bg.jpg);">
		<div class="container-md" style="background-color: #00bcd4  " style="position: center" >
	<p>&nbsp;</p>
	<div class="row">
	  <div class="col"></div>
	  <div class="col">
	  	<form name="voltar" action="index.html">
	  	<p class="text-md-center" style="color: white">
		<button type="submit" name="voltarindex" class="btn btn-secondary">Voltar</button>
		</p>
		</form>
	  </div>
	  <div class="col"></div>
	</div>
	<div class="row">
	  <div class="col"></div>
	  <div class="col">
	  	<?php
//cabeçalho e crianção tabela
echo "<table border='1' style='color:#FFFFFF;'>";
echo "<tr style='color:#FFFFFF;'>";
echo "<th>Media no Bairro</th>";
echo "</tr>";

//pegando a variavel que vem do html
$bairro = $_POST['bairro'];
 
//realizando conexão com o banco de dados
$strcon = mysqli_connect('localhost','root', '4991','imobiliaria') or die ('ERRO AO TENTAR CONEXÃO COM O BANCO DE DADOS');
$sql = "SELECT AVG(round(valorBD)) FROM apartamento WHERE bairroBD='$bairro'";
$resultado = mysqli_query($strcon,$sql) or die ("ERRO AO CONSULTAR O BANCO DE DADOS");

while($registro = mysqli_fetch_array($resultado))
{
	$media = $registro['AVG(round(valorBD))'];
	echo"<tr>";
	echo "<td>".$media."</td>";
	echo"</tr>";
}
mysqli_close($strcon);
echo "</table>";
?>
	  </div>
	  <div class="col"></div>
	</div>
<!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</body>
</html>