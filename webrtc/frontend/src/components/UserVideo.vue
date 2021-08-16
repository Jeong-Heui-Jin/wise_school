<template>
<div v-if="streamManager">
	<ov-video :stream-manager="streamManager"/>
	<div class="video-name-wrapper">
		<p v-if="streamManager.handUp" style="background-color:red;">{{ clientData }}</p>
		<p v-else>{{ clientData }}</p>
	</div>
</div>
</template>

<script>
import OvVideo from './OvVideo';

export default {
	name: 'UserVideo',

	components: {
		OvVideo,
	},

	props: {
		streamManager: Object,
	},

	computed: {
		clientData () {
			const { clientData } = this.getConnectionData();
			return clientData;
		},
	},

	methods: {
		getConnectionData () {
			const { connection } = this.streamManager.stream;
			return JSON.parse(connection.data);
		},
	},
};
</script>
