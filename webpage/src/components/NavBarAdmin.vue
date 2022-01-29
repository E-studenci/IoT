<template>
    <div>
	    <b-nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <b-img :src="require('../../static/images/logo.jpg')" width="50" height="30"/>
            <a class="navbar-brand" href="#"> Klub fitness</a>
            <b-nav-item class="nav-item active">
                <router-link style="color: #efefef; text-decoration: none;" to="/currentClients">Obecni klienci</router-link>
            </b-nav-item>
            <b-nav-item class="nav-item active">
                <router-link style="color: #efefef; text-decoration: none;" to="/allClients">Wszyscy klienci</router-link>
            </b-nav-item>
            <b-nav-item class="nav-item active">
                <router-link style="color: #efefef; text-decoration: none;" to="/addClient">Dodaj klienta</router-link>
            </b-nav-item>
            <b-button class="btn text-right" @click="logout" id="logoutBtn">Wyloguj</b-button>
        </b-nav>	 
    </div>
</template>

<script>
export default {
    methods: {
        logout() {
            var myHeaders = new Headers();
            myHeaders.append("Cookie", document.cookie);

            var requestOptions = {
                method: 'GET',
                headers: myHeaders,
                credentials: 'include',
            };

            fetch(this.$development + "logout", requestOptions)
            .then(res => {
                if(res.ok) {
                    document.cookie = 'session=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
                    this.$router.push('/login')
                }
            })
        }
    }
}
</script>

<style>
#logoutBtn {
    margin-left: 450px;
}
router-link {
    color: white
}
</style>
