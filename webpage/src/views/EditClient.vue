<template>
  <div>
      <NavBarAdmin />
      <div class="content">
		<h2>Dane klienta</h2><br/><br/>
			<p>
				<label>Imie </label>
			</p>
			<p>
				<input id="name" value="" size="30" pattern="[A-Z][a-z]+" required="true"
				title="Imie musi zaczynać się duża literą!" placeholder="Wprowadź imie"/>
			</p>
			<p>
				<label>Nazwisko </label>
			</p>
			<p>
				<input id="surname" value="" size="30" pattern="[A-Z][a-z]+" required="true"
				title="Nazwisko musi zaczynać się duża literą!" placeholder="Wprowadź nazwisko"/>
			</p>
			<p>
				<label id=emailLable>E-mail </label>
			</p>
			<p>
				<input id="email" value=""  size="30" required="true"
				pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
				title="E-mail musi mieć odpowiedni format!" placeholder="Wprowadź e-mail"/>
			</p>
			<p>
				<label id=cardLable>Karnet </label>
			</p>
			<p>
				<input id="karnetId" value=""/>
				<input type="button" id="karnetR" value="Usuń" v-on:click="removeCard()"/>
				<input type="hidden" id="karnetA" value="Przypisz" v-on:click="assignCard()"/>
			</p><br/>
			<p>
				<input type="button" onClick="history.back();" value="Powrót"/>
				<input type="button" @click="editClient(id)" value="Zatwierdź"/>
			</p>
	</div>
  </div>
</template>

<script>
import NavBarAdmin from '../components/NavBarAdmin.vue'

export default {
    components: {
        NavBarAdmin
    },
    methods: {
		editClient(id) {
			var name = document.getElementById('name');
			var surname = document.getElementById('surname');
			var email = document.getElementById('email');
			var card = document.getElementById('karnetId');
			var doc = {};
			
			if (name.value != "" && name.value != this.nameData){
				doc = { "name": name.value };
				if (surname.value != "" && surname.value != this.surnameData){
					doc = { "surname": surname.value,"name": name.value};
					if (email.value != "" && email.value != this.emailData){
						doc = { "surname": surname.value, "name": name.value, "email": email.value };}
						if(card.value != this.cardData){
							doc = { "surname": surname.value, "name": name.value, "email": email.value, "card": card.value};}}
				else if (email.value != "" && email.value != this.emailData){
					doc = {"name": name.value, "email": email.value };}
					if(card.value != this.cardData){
						doc = { "name": name.value, "email": email.value, "card": card.value};}}
			else if (surname.value != "" && surname.value != this.surnameData){
				doc = { "surname": surname.value };
				if (email.value != "" && email.value != this.emailData){
					doc = { "surname": surname.value, "email": email.value };}
					if(card.value != this.cardData){
						doc = { "surname": surname.value, "email": email.value, "card": card.value};}}
			else if (email.value != "" && email.value != this.emailData){
				doc = { "email": email.value };
				if(card.value != this.cardData){
					doc = {"email": email.value, "card": card.value};}}
			else if(card.value != this.cardData){
				doc = {"card": card.value};}

				console.log(doc);
				var myHeaders = new Headers();
				myHeaders.append("Cookie", document.cookie);
				myHeaders.append("Content-Type", "application/json");
				var requestOptions = {
					method: 'PATCH',
					headers: myHeaders,
					credentials: 'include',
					body: JSON.stringify(doc)
				};
				var code = 0;
				fetch(this.$development + "user/edit/"+id, requestOptions)
				.then((res) => {
					if(res.ok) {
						this.$router.push('/allClients');
						return res.json()
					}
					else if(res.status == '401') {
						this.$router.push('/login')
					}
				})
				.then(data => console.log('Success:', data))
				.catch(error => console.log('error', error));
    },
		removeCard(){
			this.cardData = " ";
			document.getElementById("karnetId").setAttribute("type", "hidden");
			document.getElementById("karnetId").setAttribute("value", "");
			document.getElementById("karnetR").setAttribute("type", "hidden");
			document.getElementById("karnetA").setAttribute("type", "button");

	},
		assignCard(){
			var myHeaders = new Headers();
			myHeaders.append("Cookie", document.cookie);
			myHeaders.append("Content-Type", "application/json");
			var requestOptions = {
				method: 'GET',
				headers: myHeaders,
				credentials: 'include',
			};
			var code = 0;
			fetch(this.$development + "utils/get_scanned_card", requestOptions)
			.then((res) => {
				code = res.status;
				if(res.ok) {
                    var err = document.getElementById("cardLable");
					err.innerHTML =  "Karnet";
					err.style.setProperty("color", "white");
					return res.json()
				}
				else if(code == '401') {
					this.$router.push('/login')
				}
				else if(code == '400') {
                    var err = document.getElementById("cardLable");
					err.innerHTML =  "Brak karty na czytniku, przyłóż kartę";
					err.style.setProperty("color", "red");
				}
			})
			.then(result => {
			if (code >= 200 && code < 400){
				document.getElementById("karnetId").setAttribute("type", "text");
				document.getElementById("karnetA").setAttribute("type", "hidden");
				document.getElementById("karnetR").setAttribute("type", "button");
				var card = document.getElementById('karnetId');
				card.setAttribute("value", result.data.rfid);
				this.card = result.data.rfid;
			}})
				.catch(error => console.log('error', error));

	},
		loadData(id) {
		var myHeaders = new Headers();
		myHeaders.append("Cookie", document.cookie);
		var requestOptions = {
			method: 'GET',
			headers: myHeaders,
			credentials: 'include',
		};
		var code = 0;
		fetch(this.$development + "user/get/"+id, requestOptions)
			 .then((res) => {
				code = res.status;
				if(res.ok) {
					return res.json()
				}
				else if(res.status == '401') {
					this.$router.push('/login')
				}
			})
			.then(result => {
			if (code >= 200 && code < 400){
					var name = document.getElementById('name');
					name.setAttribute("value", result.data.name);
					this.nameData = result.data.name;
					var surname = document.getElementById('surname');
					surname.setAttribute("value", result.data.surname);
					this.surnameData = result.data.surname;
					var email = document.getElementById('email');
					email.setAttribute("value", result.data.email);
					this.emailData = result.data.email;
					var card = document.getElementById('karnetId');
					if (result.data.card == "") {
						document.getElementById("karnetId").setAttribute("type", "hidden");
						document.getElementById("karnetR").setAttribute("type", "hidden");
						document.getElementById("karnetA").setAttribute("type", "button");
						var button = document.getElementById("karnet");
						button.setAttribute("value", "Przypisz");
						button.setAttribute("v-on:click", "assignCard()");
					} else {
						document.getElementById("karnetId").setAttribute("type", "text");
						document.getElementById("karnetA").setAttribute("type", "hidden");
						document.getElementById("karnetR").setAttribute("type", "button");
						card.setAttribute("value", result.data.card);
						this.cardData = result.data.card;
					}
			
			} else {
				console.log('error');
			}
		})
		.catch(error => console.log('error', error));
		}
		},
    data() {
		id = "",
		nameData = "",
		surnameData = "",
		emailData = "",
		cardData = ""
    },
    mounted() {
		var queryString = window.location.search;
		var urlParams = new URLSearchParams(queryString);
		this.id = urlParams.get('id');
        this.loadData(this.id);
    }
}
</script>

<style>
.content
{
	text-align: center;
	padding: 10px;
}
tbody
{
    cursor: pointer;
}
</style>