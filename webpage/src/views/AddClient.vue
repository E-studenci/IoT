<template>
  <div>
      <NavBarAdmin />
	  <div class="content">
		<h2>Dodaj Klienta</h2><br/><br/>
			<p>
				<label>Imie </label>
			</p>
			<p>
				<input id="name" size="30" pattern="[A-Z][a-z]+" required="true"
				title="Imie musi zaczynać się duża literą" placeholder="Wprowadź imie"/>
			</p>
			<p>
				<label>Nazwisko </label>
			</p>
			<p>
				<input id="surname"  size="30" pattern="[A-Z][a-z]+" required="true"
				title="Nazwisko musi zaczynać się duża literą!" placeholder="Wprowadź nazwisko"/>
			</p>
			<p>
				<label id=emailLable>E-mail </label>
			</p>
			<p>
				<input id="email" size="30"
				pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" required="true"
				title="E-mail musi mieć odpowiedni format!" placeholder="Wprowadź e-mail"/>
			</p>
			<p>
				<label id=cardLable>Karnet </label>
			</p>
			<p>
				<input type="hidden" id="karnetId" value=""/>
				<input type="hidden" id="karnetR" value="Usuń" v-on:click="removeCard()"/>
				<input type="button" id="karnetA" value="Przypisz" v-on:click="assignCard()"/>
			</p><br/>
			<p>
				<input type="button" onclick="history.back();" value="Powrót"/>
				<input type="submit" @click="addClient()" value="Dodaj"/>
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
        addClient() {
		var name = document.getElementById('name');
		var surname = document.getElementById('surname');
		var email = document.getElementById('email');
		var card = document.getElementById('karnetId');
		
		if (name.value != "" && surname.value != "" && email.value != "") {
			var doc = {
					name: name.value,
					surname: surname.value,
					email: email.value,
					status: "ACTIVE",
					card: card.value
				};
			console.log(doc);
			var myHeaders = new Headers();
			myHeaders.append("Cookie", document.cookie);
			myHeaders.append("Content-Type", "application/json");
			var requestOptions = {
				method: 'PUT',
				headers: myHeaders,
				credentials: 'include',
				body: JSON.stringify(doc)
			};
		fetch("http://130.61.111.97:20001/user/get/"+id, requestOptions)
			fetch("/user/add", requestOptions)
			.then((res) => {
				if(res.ok) {
					console.log('Success:', res);
					this.$router.push('/allClients');
					res => res.json();
                    return res.json()
                }
                else if(res.status == '401') {
                    this.$router.push('/login');
                }
                else if(res.status == '400') {
                    var err = document.getElementById("emailLable");
					err.innerHTML =  "Ten emeil już istnieje, podaj inny";
					err.style.setProperty("color", "red");
                }
			})
			.then(data => element.innerHTML = data.updatedAt)
			.catch(error => console.log('error', error));
		
		}
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
			fetch("http://130.61.111.97:20001/utils/get_scanned_card", requestOptions)
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
