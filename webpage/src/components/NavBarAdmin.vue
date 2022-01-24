<template>
    <div>
	    <b-nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <b-img :src="require('../../static/images/logo.jpg')" width="50" height="30"/>
            <a class="navbar-brand" href="#"> Siłownia fitness</a>
            <b-nav-item class="nav-item active">
                <router-link style="color: #efefef; text-decoration: none;" to="/currentClients">Obecni klienci</router-link>
            </b-nav-item>
            <b-nav-item class="nav-item active">
                <router-link style="color: #efefef; text-decoration: none;" to="/allClients">Wszyscy klienci</router-link>
            </b-nav-item>
            <b-nav-item class="nav-item active">
                Dodaj klienta
            </b-nav-item>
            <b-button class="btn text-right" @click="logout" id="logoutBtn">Wyloguj</b-button>
        </b-nav>	 
    </div>
</template>

<script>
export default {
    methods: {
        logout() {
            //console.log("laalal")
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