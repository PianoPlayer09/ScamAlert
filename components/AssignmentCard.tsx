import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function AssignmentCard({ title, dueDate }: { title: string; dueDate: string }) {
  return (
    <View style={styles.card}>
      <Text style={styles.title}>{title}</Text>
      <Text style={styles.dueDate}>Due: {dueDate}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    borderRadius: 8,
    padding: 16,
    marginVertical: 8,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  dueDate: {
    fontSize: 14,
    color: '#666',
  },
});
