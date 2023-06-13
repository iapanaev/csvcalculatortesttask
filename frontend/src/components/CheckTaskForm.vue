<script setup>
import { reactive } from 'vue'

var state = reactive({
  task_id: '',
  error: '',
  loading: false,
  result: null
})

async function submit() {
  state.error = ''
  state.result = null
  if(state.task_id === '') {
    state.error = 'Введите ID задачи'
    return
  }
  if(/[\D]/.test(state.task_id)) {
    state.error = 'Невалидный ID задачи'
    return
  }
  state.loading = true
  try {
    const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/${state.task_id}/`)
    const data = await response.json()
    if(response.status !== 200) {
      state.error = data.detail ? data.detail : 'Неизвестная ошибка'
    } else {
      state.result = data
    }
  } catch(error) {
    state.error = 'Ошибка при отправке/получении запроса'
  } finally {
    state.loading = false
  }
}
</script>

<template>
  <h2>Инфо задачи</h2>
  <form @submit.prevent="submit">
    <fieldset :disabled="state.loading">
      <div class="mb-2">
        <label for="taskIdInput" class="form-label">ID Задачи</label>
        <input
          placeholder="Введите имя файла"
          v-model="state.task_id"
          type="text"
          class="form-control"
          id="taskIdInput" />
        <div class="form-text text-danger" v-if="state.error">{{ state.error }}</div>
      </div>
      <button type="submit" class="btn btn-primary">Получить данные</button>
    </fieldset>
  </form>
  <div v-if="state.result">
    <p>Данные:</p>
    <code><pre>{{ JSON.stringify(state.result, null, "  ") }}</pre></code>
  </div>
</template>
