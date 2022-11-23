function func() {
	var data = document.getElementById("input").value;
	data.replace(" ","+");
	console.log(data);
	var sitetogo = "http://localhost:8080/"+data;
	location.replace(sitetogo);
};
