<template>
    <p>Counter: {{ counter }}</p>

    <button @click="reset">Reset</button>
    <button @click="terminate">☠️</button>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    const counter = ref(0)

    const interval = setInterval(() => {
      counter.value++
    }, 1000)

    const reset = () => {
      counter.value = 0
    }

    const terminate = () => {
      clearInterval(interval)
    }

    return {
      counter,
      reset,
      terminate
    }
  }
}
</script>