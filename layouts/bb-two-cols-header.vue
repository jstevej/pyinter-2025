<!--
  Usage:
```md
---
layout: two-cols-header
---
This spans both
::left::
# Left
This shows on the left
::right::
# Right
This shows on the right
```
-->

<script setup lang="ts">
const props = defineProps({
  class: {
    type: String,
  },
  layoutClass: {
    type: String,
  },
})
</script>

<template>
  <div class="slidev-layout bb-two-cols-container w-full h-full" :class="layoutClass">
    <div class="bb-header">
      <slot />
    </div>
    <div class="bb-columns">
      <div class="bb-left" :class="props.class">
        <slot name="left" />
      </div>
      <div class="bb-right" :class="props.class">
        <slot name="right" />
      </div>
    </div>
    <div class="bb-bottom">
        <slot name="bottom" />
    </div>
  </div>
</template>

<style scoped>
.bb-two-cols-container {
  display: flex;
  flex-direction: column;
}

.bb-header {
}

.bb-columns {
  flex-grow: 1;
  display: grid;
  column-gap: 25px;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr;
}

.bb-left {
  align-self: start;
  grid-area: 1 / 1 / 2 / 2;
}

.bb-right {
  align-self: start;
  grid-area: 1 / 2 / 2 / 3;
}

.bb-bottom {
}

</style>
