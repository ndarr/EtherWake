const base_url = "http://ubuntu-pi.lan:5000/";



const vm = new Vue({
    el: '#app',
    data: {
      results: []
    },
    methods:{
      wakeUp: function wakeUp(device){
        let url = base_url + "wakeup/" + device;
        console.log("Waking: " + device);
        axios.get(url).then((response) => {
          msg = response.data;
          alert(msg)
        }).catch( error => { alert("Oops, something went wrong!"); });}
    },
    mounted() {
      axios.get(base_url)
      .then(response => {this.results = response.data})
    }
  });
