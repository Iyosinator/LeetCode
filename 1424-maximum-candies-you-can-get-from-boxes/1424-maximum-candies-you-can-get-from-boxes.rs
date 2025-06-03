use std::collections::{VecDeque, HashSet};

impl Solution {
    pub fn max_candies(
        status: Vec<i32>,
        candies: Vec<i32>,
        keys: Vec<Vec<i32>>,
        contained_boxes: Vec<Vec<i32>>,
        initial_boxes: Vec<i32>,
    ) -> i32 {
        let n = status.len();
        let mut visited = vec![false; n];
        let mut has_key = vec![false; n];
        let mut boxes = vec![false; n];
        
        let mut queue = VecDeque::new();
        for &b in &initial_boxes {
            boxes[b as usize] = true;
            if status[b as usize] == 1 {
                queue.push_back(b);
            }
        }
        
        let mut total_candies = 0;

        while let Some(box_id) = queue.pop_front() {
            let box_id = box_id as usize;

            if visited[box_id] {
                continue;
            }
            visited[box_id] = true;

            total_candies += candies[box_id];

            for &k in &keys[box_id] {
                let k = k as usize;
                has_key[k] = true;
            
                if boxes[k] && !visited[k] {
                    queue.push_back(k as i32);
                }
            }

            for &b in &contained_boxes[box_id] {
                let b = b as usize;
                boxes[b] = true;
                if (status[b] == 1 || has_key[b]) && !visited[b] {
                    queue.push_back(b as i32);
                }
            }
        }

        total_candies
    }
}
