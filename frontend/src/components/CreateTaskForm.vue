<script setup>
import { reactive } from 'vue'

var state = reactive({
  filename: '',
  error: '',
  loading: false,
  result: null
})

async function submit() {
  state.error = ''
  state.result = null
  if(state.filename === '') {
    state.error = 'Введите название файла'
    return
  }
  state.loading = true
  try {
    const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ filename: state.filename })
    })
    const data = await response.json()
    if(response.status !== 201) {
      state.error = data.filename ? data.filename.join(', ') : data.detail ? data.detail : 'Неизвестная ошибка'
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
  <h2>Создать задачу</h2>
  <form @submit.prevent="submit">
    <fieldset :disabled="state.loading">
      <div class="mb-2">
        <label for="fileNameInput" class="form-label">Имя файла</label>
        <input
          placeholder="Введите имя файла"
          v-model="state.filename"
          type="text"
          class="form-control"
          id="fileNameInput" />
        <div class="form-text text-danger" v-if="state.error">{{ state.error }}</div>
      </div>
      <button type="submit" class="btn btn-primary">Создать задачу</button>
    </fieldset>
  </form>
  <div v-if="state.result">ID задачи: {{ state.result.id }}</div>
</template>
