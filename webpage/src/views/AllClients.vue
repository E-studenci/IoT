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
                <th scope="col">Stan konta</th>
                <th scope="col">Nr karty</th>
              </tr>
            </thead>
            <tbody v-for="client in allClients" :key="client._id">
              <tr class="table-secondary" onclick="window.location='#';">
                <th scope="row">{{ client._id }}</th>
                <td>{{ client.surname }}</td>
                <td>{{ client.name }}</td>
                <td>{{ client.email }}</td>
                <td>{{ client.balance }}</td>
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
    data() {
        return {
            allClients: [
        {
            "_id": "61e750e6ecd8897aa62de661",
            "surname": "Snow",
            "name": "Zidan",
            "balance": 3000,
            "email": "example1@gmail.com",
            "status": "ACTIVE",
            "card": "f91a61e515d1fc6a7fa9986473b6d0ff",
            "current_visit": {
                "_id": "61e751c6e2ed2b9d91a86880",
                "visit_start": "2022/01/18 23:48:22",
                "cost_per_min": 70,
                "visit_type": {
                    "_id": "61e750ddecd8897aa62de65b",
                    "visit_type": "Pool",
                    "cost_per_min": 70,
                    "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
                }
            }
        },
        {
            "_id": "61e750e6ecd8897aa62de662",
            "surname": "Sean",
            "name": "Buckley",
            "balance": 7000,
            "email": "example2@gmail.com",
            "status": "ACTIVE",
            "card": "9827bce49e2b5b9ea09f69db59c20e85",
            "current_visit": {
                "_id": "61e7519ee2ed2b9d91a8687e",
                "visit_start": "2022/01/18 23:47:42",
                "cost_per_min": 70,
                "visit_type": {
                    "_id": "61e750ddecd8897aa62de65b",
                    "visit_type": "Pool",
                    "cost_per_min": 70,
                    "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
                }
            }
        },
        {
            "_id": "61e750e6ecd8897aa62de663",
            "surname": "Jolene",
            "name": "Alvarado",
            "balance": 1000,
            "email": "example3@gmail.com",
            "status": "ACTIVE",
            "card": "85bc3f25732df73426aa44f59c6ec78c"
        },
        {
            "_id": "61e750e6ecd8897aa62de664",
            "surname": "Maxim",
            "name": "Witt",
            "balance": 2000,
            "email": "example4@gmail.com",
            "status": "ACTIVE",
            "card": "bdef2adeeede3e4502c6d891b0a0e3e4",
            "current_visit": {
                "_id": "61e751eee2ed2b9d91a86881",
                "visit_start": "2022/01/18 23:49:02",
                "cost_per_min": 70,
                "visit_type": {
                    "_id": "61e750ddecd8897aa62de65b",
                    "visit_type": "Pool",
                    "cost_per_min": 70,
                    "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
                }
            }
        },
        {
            "_id": "61e750e6ecd8897aa62de665",
            "surname": "Tylor",
            "name": "Santiago",
            "balance": 5000,
            "email": "example5@gmail.com",
            "status": "DISABLED",
            "card": "44963461cf009e75c11447da27aec4ed",
            "current_visit": {
                "_id": "61e751bce2ed2b9d91a8687f",
                "visit_start": "2022/01/18 23:48:12",
                "cost_per_min": 70,
                "visit_type": {
                    "_id": "61e750ddecd8897aa62de65b",
                    "visit_type": "Pool",
                    "cost_per_min": 70,
                    "rfid_scanner": "9827bce49e2b5b9ea09f69db59c20e85"
                }
            }
        }
    ]}}
}
</script>

<style>
#allClientsTable
{
    padding-left: 50px;
    padding-right: 50px;
    padding-top: 30px;
    margin-top: 10px;
    color: black;
}
tbody
{
    cursor: pointer;
}
</style>