<template>
  <div>
      <NavBarAdmin />
      <div class="allClientsTable">
        <table class="table table-striped table-hover">
            <thead>
              <tr class="table-secondary">
                <th scope="col">Nr klienta</th>
                <th scope="col">Nazwisko</th>
                <th scope="col">Imię</th>
                <th scope="col">Email</th>
                <th scope="col">Nr karty</th>
              </tr>
            </thead>
            <tbody v-for="client in allClients" :key="client._id">
              <tr class="table-secondary" @click="editClientData(client._id)">
                <th scope="row">{{ client._id }}</th>
                <td>{{ client.surname }}</td>
                <td>{{ client.name }}</td>
                <td>{{ client.email }}</td>
                <td>{{ client.card }}</td>
              </tr>
            </tbody>
        </table>
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
        findAllCLients() {
            var myHeaders = new Headers();
            myHeaders.append("Cookie", document.cookie);
            
            var requestOptions = {
                method: 'GET',
                headers: myHeaders,
                credentials: 'include',
            };

		    fetch(this.$development + "user/get", requestOptions)
            .then((res) => {
                if(res.ok) {
                    return res.json()
                }
                else if(res.status == '401') {
                    this.$router.push('/login')
                }
            })
            .then(data => {
                console.log(data)
                this.allClients = data.data
            })
        },
	    editClientData(id) {
			  this.$router.push('/editClient?id='+id);
	    }
    },
    data() {
        return {
            allClients: []
        }
    },
    mounted() {
        this.findAllCLients()
    }
}
</script>

<style>
#allClientsTable
{
    padding-left: 50px;
    padding-right: 50px;
    color: black;
}
tbody
{
    cursor: pointer;
}
</style>
