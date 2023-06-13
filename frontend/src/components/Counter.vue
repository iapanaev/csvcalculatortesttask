<script setup>
import { onMounted, onUnmounted, reactive } from 'vue'

var interval = null

var state = reactive({
  running: 0,
  queued: 0,
  error: ''
})

onMounted(() => {
  interval = setInterval(() => {
    fetch(`${import.meta.env.VITE_API_BASE_URL}/running_tasks_count/`).then(response => {
      response.json().then(data => {
        if(data.running !== undefined  && data.queued !== undefined) {
          state.running = data.running
          state.queued = data.queued
          state.error = ''
        } else {
          state.error = 'Невалидный ответ'
        }
      }).catch(() => {
        state.error = 'Ошибка при обработке ответа'
      })
    }).catch(() => {
      state.error = 'Ошибка при отправке/получении запроса'
    })
  }, 1000)
})

onUnmounted(() => {
  clearInterval(interval)
})
</script>

<template>
  <h1 class="text-center">Запущенных задач: {{ state.running }}</h1>
  <h1 class="text-center">Задач в очереди: {{ state.queued }}</h1>
  <div class="alert alert-danger" role="alert" v-if="state.error">
    {{ state.error }}
  </div>
</template>
