<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'

import { ref, onMounted } from 'vue'

const apiData = ref(null)

onMounted(async () => {
  try {
    const response = await fetch('/__backend/api/data')
    let data = await response.json()
    console.log('Fetched data:', data)
    apiData.value = data.users || { message: 'No data available' }
  } catch (error) {
    console.error('Failed to fetch data:', error)
  }
})

</script>

<template>
  Hello World!
  {{
    apiData
  }}
</template>