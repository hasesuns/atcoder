use proconio::input;

fn main() {
    input! {
        n: u32,
        a: [i64; 2usize.pow(n as u32)],
    }
    let (i_first, v_first) = &a[0..2usize.pow(n - 1)].iter().enumerate().fold(
        (std::usize::MIN, std::i64::MIN),
        |(i_aa, aa), (i_bb, &bb)| {
            if bb > aa {
                (i_bb, bb)
            } else {
                (i_aa, aa)
            }
        },
    );
    let (i_second, v_second) = &a[2usize.pow(n - 1)..2usize.pow(n)].iter().enumerate().fold(
        (std::usize::MIN, std::i64::MIN),
        |(i_aa, aa), (i_bb, &bb)| {
            if bb > aa {
                (i_bb, bb)
            } else {
                (i_aa, aa)
            }
        },
    );
    if v_first >= v_second {
        println!("{}", i_second + 2usize.pow(n - 1) + 1)
    } else {
        println!("{}", i_first + 1)
    }
}