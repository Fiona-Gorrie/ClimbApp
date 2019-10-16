<template>
  <div class="hello">
    <h1>{{ title }}</h1>

    <h1>Climb Type</h1>

    <form action="">
      <input type="checkbox" name="Trad" value="Trad">Trad<br>
      <input type="checkbox" name="Sport" value="Sport">Sport<br>
      <input type="checkbox" name="Some Gear" value="Some Gear">Some Gear<br>
      <input type="checkbox" name="Top Rope" value="Top Rope" checked>Top Rope<br><br>
    </form>

    <h2>From Grade</h2>
    <select>
      <option value="3rd">3rd</option>
      <option value="4th">4th</option>
      <option value="5.0">5.0</option>
      <option value="5.1">5.1</option>
      <option value="5.2">5.2</option>
      <option value="5.3">5.3</option>
      <option value="5.4">5.4</option>
      <option value="5.5">5.5</option>
      <option value="5.6">5.6</option>
      <option value="5.7">5.7</option>
      <option value="5.8">5.8</option>
      <option value="5.9">5.9</option>
      <option value="5.10a">5.10a</option>
      <option value="5.10b">5.10b</option>
      <option value="5.10c">5.10c</option>
      <option value="5.10d">5.10d</option>
      <option value="5.11a">5.11a</option>
      <option value="5.11b">5.11b</option>
      <option value="5.11c">5.11c</option>
      <option value="5.11d">5.11d</option>
      <option value="5.12a">5.12a</option>
      <option value="5.12b">5.12b</option>
      <option value="5.12c">5.12c</option>
      <option value="5.12d">5.12d</option>
      <option value="5.13a">5.13a</option>
      <option value="5.13b">5.13b</option>
      <option value="5.13c">5.13c</option>
      <option value="5.13d">5.13d</option>
      <option value="5.14a">5.14a</option>
      <option value="5.14b">5.14b</option>
      <option value="5.14c">5.14c</option>
      <option value="5.14d">5.14d</option>
      <option value="5.15a">5.15a</option>
      <option value="5.15b">5.15b</option>
      <option value="5.15c">5.15c</option>
      <option value="5.15d">5.15d</option>            
    </select>

    <h2>To Grade</h2>
    <select>
      <option value="3rd">3rd</option>
      <option value="4th">4th</option>
      <option value="5.0">5.0</option>
      <option value="5.1">5.1</option>
      <option value="5.2">5.2</option>
      <option value="5.3">5.3</option>
      <option value="5.4">5.4</option>
      <option value="5.5">5.5</option>
      <option value="5.6">5.6</option>
      <option value="5.7">5.7</option>
      <option value="5.8">5.8</option>
      <option value="5.9">5.9</option>
      <option value="5.10a">5.10a</option>
      <option value="5.10b">5.10b</option>
      <option value="5.10c">5.10c</option>
      <option value="5.10d">5.10d</option>
      <option value="5.11a">5.11a</option>
      <option value="5.11b">5.11b</option>
      <option value="5.11c">5.11c</option>
      <option value="5.11d">5.11d</option>
      <option value="5.12a">5.12a</option>
      <option value="5.12b">5.12b</option>
      <option value="5.12c">5.12c</option>
      <option value="5.12d">5.12d</option>
      <option value="5.13a">5.13a</option>
      <option value="5.13b">5.13b</option>
      <option value="5.13c">5.13c</option>
      <option value="5.13d">5.13d</option>
      <option value="5.14a">5.14a</option>
      <option value="5.14b">5.14b</option>
      <option value="5.14c">5.14c</option>
      <option value="5.14d">5.14d</option>
      <option value="5.15a">5.15a</option>
      <option value="5.15b">5.15b</option>
      <option value="5.15c">5.15c</option>
      <option value="5.15d">5.15d</option>            
    </select>

    <h2>Rating</h2>
  
    &star;
    &star;
    &star;
    &star;

  </div>
  
</template>

<script>
export default {
  name: 'ClimbApp',
  props: ['title'],
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
