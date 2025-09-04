<script setup lang="ts">
import { computed } from 'vue'
import { handleBackground } from '../theme/layoutHelper'
const props = defineProps({
    background: {
        // random image from a curated Unsplash collection by Anthony
        default: 'https://source.unsplash.com/collection/94734566/1920x1080',
    },
})
const style = computed(() => handleBackground(props.background, true))
</script>

<template>
    <div class="slidev-layout bb-cover-outer cover" :style="style">
        <div class="bb-cover-inner">
            <slot />
        </div>
    </div>
</template>

<style scoped>
.bb-cover-outer {
    width: 100%;
    display: flex;
    justify-content: center;
}

.bb-cover-inner {
}
</style>
