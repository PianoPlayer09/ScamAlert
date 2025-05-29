import { StatusBar } from 'expo-status-bar';
import { StyleSheet } from 'react-native';
import { Text, View } from '@/components/Themed';

export default function ScamAlertModal() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Scam Alert</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      {/* Future: Show scam notification details here */}
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
