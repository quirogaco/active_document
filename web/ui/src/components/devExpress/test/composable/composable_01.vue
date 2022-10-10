<template>
  X: {{ x }} Y: {{ y }}
</template>

<script setup>
  import { useMouse } from './useMouse';
  const { x, y } = useMouse();
</script>