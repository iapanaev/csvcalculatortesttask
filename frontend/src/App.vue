<script setup>
import CheckTaskForm from './components/CheckTaskForm.vue'
import Counter from './components/Counter.vue'
import CreateTaskForm from './components/CreateTaskForm.vue'
</script>

<template>
  <div class="container-md">
    <div class="row mb-3 mt-3">
      <div class="col">
        <Counter />
      </div>
    </div>
    <hr />
    <div class="row">
      <div class="col-12 col-sm-6">
        <CreateTaskForm />
      </div>
      <div class="col-12 col-sm-6">
        <CheckTaskForm />
      </div>
    </div>
  </div>
</template>