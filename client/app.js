const base_url = "http://localhost:5000/";



const vm = new Vue({
    el: '#app',
    data: {
      results: [],
      showModal: false
    },
    methods:{
      wakeUp: function wakeUp(device){
        let url = base_url + "wakeup/" + device;
        console.log("Waking: " + device);
        axios.get(url).then((response) => {
          msg = response.data;
          alert(msg)
        }).catch( error => { alert("Oops, something went wrong!"); });},
        addDialog: function addDialog(){
          alert("click");
        },
      addDevice: function (name, mac) {
        let url = base_url + "device";
        axios.post(url, {name: name, mac: mac}).then((response) => {
          msg = response.data;
          alert(msg)
        }).catch( error => { alert("Oops, something went wrong!"); });},
    },
    mounted() {
      axios.get(base_url)
      .then(response => {this.results = response.data})
    }
  });
  
  
  
  Vue.component('modal', {
    template: '#modal-template',
    props: ['show', 'name', 'mac'],
    methods: {
      cancel: function(){
        this.$emit('close');
      },
      savePost: function () {
        vm.addDevice(this.name, this.mac)
        this.$emit('close');
      }
    }
  });
