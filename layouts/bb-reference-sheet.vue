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
  <div class="slidev-layout bb-reference-sheet w-full h-full" :class="layoutClass">
    <div class="bb-columns">
      <div class="bb-col1" :class="props.class">
        <slot name="col1" />
      </div>
      <div class="bb-col2" :class="props.class">
        <slot name="col2" />
      </div>
      <div class="bb-col3" :class="props.class">
        <slot name="col3" />
      </div>
    </div>
  </div>
</template>

<style>

.bb-reference-sheet {
    font-size: 10px !important; /* for <br/> */
    padding: 0.4in !important;
}

.bb-columns h2 {
    font-size: 10px !important;
    line-height: 10px !important;
    padding: 8px 0 4px 0 !important;
}

.bb-columns .slidev-code-wrapper {
    margin: 0 0 0 0 !important;
}

.bb-columns .slidev-code {
    padding: 0 0 0 0 !important;
}

.bb-columns pre {
    font-size: 10px  !important;
    line-height: 12px !important;
}

.bb-two-cols-container {
  display: flex;
  flex-direction: column;
}

.bb-columns {
  flex-grow: 1;
  display: grid;
  column-gap: 12px;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr;
}

.bb-col1 {
  align-self: start;
  grid-area: 1 / 1 / 2 / 2;
}

.bb-col2 {
  align-self: start;
  grid-area: 1 / 2 / 2 / 3;
}

.bb-col3 {
  align-self: start;
  grid-area: 1 / 3 / 2 / 4;
}

.bb-col4 {
  align-self: start;
  grid-area: 1 / 4 / 2 / 5;
}

</style>
