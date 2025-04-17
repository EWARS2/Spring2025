const xhr = new XMLHttpRequest();

chr.addEventListener('load', () {
	console.log(xhr.response);
});

xhr.open('GET', 'https://supersimplebackend.dev/');
xhr.send();
