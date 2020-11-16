<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Listar por NºQuarto</title>
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
echo "<th>ID</th>";
echo "<th>BAIRRO</th>";
echo "<th>RUA</th>";
echo "<th>VALOR</th>";
echo "<th>AREA</th>";
echo "<th>QUARTOS</th>";
echo "<th>BANHEIROS</th>";
echo "<th>VAGA</th>";
echo "</tr>";
//pegando a variavel que vem do html
$quarto = $_POST['numeroQuarto'];
 
//realizando conexão com o banco de dados
$strcon = mysqli_connect('localhost','root', '4991','imobiliaria') or die ('ERRO AO TENTAR CONEXÃO COM O BANCO DE DADOS');
$sql = "SELECT * FROM apartamento WHERE quartoBD='$quarto'";
$resultado = mysqli_query($strcon,$sql) or die ("ERRO AO CONSULTAR O BANCO DE DADOS");

while($registro = mysqli_fetch_array($resultado))
{
	$id = $registro['idBD'];
	$bairro = $registro['bairroBD'];
	$rua = $registro['enderecoBD'];
	$valor = $registro['valorBD'];
	$area = $registro['areaBD'];
	$quartos = $registro['quartoBD'];
	$banheiros = $registro['banheiroBD'];
	$vaga = $registro['vagaBD'];
	echo"<tr>";
	echo "<td>".$id."</td>";
	echo "<td>".$bairro."</td>";
	echo "<td>".$rua."</td>";
	echo "<td>".$valor."</td>";
	echo "<td>".$area."</td>";
	echo "<td>".$quartos."</td>";
	echo "<td>".$banheiros."</td>";
	echo "<td>".$vaga."</td>";
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