<template>
  <div class="hello">
    <h1>{{ title }}</h1>

    <h1>Climb Type</h1>

  <!-- User selects Type of climb -->
    <select name="climbType" v-model="selectedType">
      <option
        id="climbType"  
        v-for="climbType in climbTypes"> {{climbType}} </option>            
    </select> 

    <h2>Select Grade</h2>

    <!-- User selects difficulty of climb -->
    
     <select name="selectGrade" v-model="selectedGrade">
      <option
        id="select-grade"  
        v-for="grade in grades"> {{grade}} </option>            
    </select>

    <h2>Rating</h2>

  <!-- vue star rating (npm installed) -->  
    <star-rating @rating-selected ="setRating"
                v-model="rating"
                v-bind:max-rating="4">
    </star-rating>

    <button @click="display_data">Submit</button>

    <p>{{selectedType}} {{selectedGrade}}</p>
    <ul>
      <li></li>
    </ul>
  </div>
  
</template>

<script>
import axios from 'axios';
import StarRating from 'vue-star-rating';
export default {
  name: 'ClimbApp',
  props: ['title'],
  
  data() {
    return {
      grades: [
        "5.0",
        "5.1",
        "5.2",
        "5.3",
        "5.4",
        "5.5",
        "5.6",
        "5.7",
        "5.8",
        "5.9",
        "5.10a",
        "5.10b",
        "5.10c",
        "5.10d",
        "5.11a",
        "5.11b",
        "5.11c",
        "5.11d",
        "5.12a",
        "5.12b",
        "5.12c",
        "5.12d",
        "5.13a",
        "5.13b",
        "5.13c",
        "5.13d",
        "5.14a",
        "5.14b",
        "5.14c",
        "5.14d",
        "5.15a",
        "5.15b",
        "5.15c",
        "15d"
      ],
      climbTypes: [
        "Trad",
        "Sport",
        "Some Gear",
        "Top Rope"
      ],
      selectedType: '', 
      selectedGrade: '',
      array_of_response_data: [],
      
      rating: 2
    }
  },
  components: {
    StarRating
  },
  methods: {
    onChange(event) {
      return (event.target.value)
    },
    setRating(rating){
      this.rating = rating;
      console.log(this.rating)
    },
    display_data() {
      axios.post("/climbData", {
        selected_climb_type: this.selectedType,
        selected_climb_grade: this.selectedGrade
      })
      .then(response=>( 
        this.array_of_response_data=response))
    },
    displayResult() {
      axios.get('/climbResult').then(response=>( 
        this.array_of_response_data=response));
    },  
  }
}  
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>